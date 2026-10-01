from dataclasses import dataclass

from hypothesis import given, strategies as st


# A message's kind travels out of band, like a WebSocket opcode; only its content is encoded.
@dataclass(frozen=True)
class Binary:
    content: bytes


@dataclass(frozen=True)
class Text:
    content: str


@dataclass(frozen=True)
class Transmission:
    message: Binary | Text
    cuts: tuple[bool, ...]

    def __repr__(self):
        kind = "text" if isinstance(self.message, Text) else "binary"
        sizes = [len(chunk) for chunk in split(encode(self.message), self.cuts)]
        return f"({kind}, {self.message.content!r}, {sizes})"


def encode(message):
    if isinstance(message, Text):
        return message.content.encode("utf-8")
    return message.content


def split(data, cuts):
    if not data:
        return []
    chunks = [bytearray(data[:1])]
    for byte, cut in zip(data[1:], cuts):
        if cut:
            chunks.append(bytearray([byte]))
        else:
            chunks[-1].append(byte)
    return [bytes(chunk) for chunk in chunks]


def decode(kind, chunks):
    if isinstance(kind, Text):
        # Deliberate bug: text chunks are decoded independently, so a scalar split across two chunks becomes replacement characters.
        return Text("".join(chunk.decode("utf-8", errors="replace") for chunk in chunks))
    return Binary(b"".join(chunks))


messages = st.one_of(
    st.binary(max_size=64).map(Binary),
    st.text(max_size=16).map(Text),
)


# The transport may split the encoded bytes anywhere: one flag per gap between bytes says whether a chunk boundary falls there.
@st.composite
def strategy(draw):
    message = draw(messages)
    gaps = max(len(encode(message)) - 1, 0)
    cuts = draw(st.lists(st.booleans(), min_size=gaps, max_size=gaps))
    return Transmission(message, tuple(cuts))


@given(strategy())
def test(transmission):
    chunks = split(encode(transmission.message), transmission.cuts)
    assert decode(transmission.message, chunks) == transmission.message

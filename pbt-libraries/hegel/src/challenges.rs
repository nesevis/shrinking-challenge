use hegel::TestCase;
use hegel::generators::{self as gs, Generator};

#[derive(Clone, Copy, Debug)]
pub enum Challenge {
    BinaryHeap,
    Calculator,
    ProductSequence(usize),
    Product(usize),
    Sum,
    ModularMapping,
    WeightedLinear,
    Invoice,
    InvoiceDerived,
    FloatCancellation,
    ChunkedDecoder,
    HashCollision(i64),
    HashCollisionMachine(i64),
    SnapshotStore,
}

impl Challenge {
    pub fn all() -> Vec<Self> {
        (2..=6)
            .map(Self::ProductSequence)
            .chain((2..=6).map(Self::Product))
            .chain([
                Self::Sum,
                Self::ModularMapping,
                Self::WeightedLinear,
                Self::Invoice,
                Self::InvoiceDerived,
                Self::FloatCancellation,
                Self::ChunkedDecoder,
                Self::HashCollision(10),
                Self::HashCollision(100),
                Self::HashCollision(1000),
                Self::SnapshotStore,
                Self::HashCollisionMachine(10),
                Self::HashCollisionMachine(100),
                Self::HashCollisionMachine(1000),
            ])
            .collect()
    }

    /// Also lists standalone ports outside the published 100-seed comparison.
    pub fn available() -> Vec<Self> {
        Self::all()
            .into_iter()
            .chain([Self::BinaryHeap, Self::Calculator])
            .collect()
    }

    pub fn name(self) -> String {
        match self {
            Self::BinaryHeap => "binheap".into(),
            Self::Calculator => "calculator".into(),
            Self::ProductSequence(depth) => format!("nested_flatmap_product_sequence_{depth}"),
            Self::Product(depth) => format!("nested_flatmap_product_{depth}"),
            Self::Sum => "nested_flatmap_sum_4".into(),
            Self::ModularMapping => "modular_mapping".into(),
            Self::WeightedLinear => "weighted_linear_preservation".into(),
            Self::Invoice => "invoice_discount".into(),
            Self::InvoiceDerived => "invoice_discount_derived".into(),
            Self::FloatCancellation => "float_cancellation".into(),
            Self::ChunkedDecoder => "chunked_decoder".into(),
            Self::HashCollision(m) => format!("hash_collision_{m}"),
            Self::HashCollisionMachine(m) => format!("hash_collision_state_machine_{m}"),
            Self::SnapshotStore => "snapshot_store".into(),
        }
    }

    pub fn is_state_machine(self) -> bool {
        matches!(self, Self::HashCollisionMachine(_) | Self::SnapshotStore)
    }

    pub fn evaluate(self, tc: &TestCase) -> (String, bool) {
        match self {
            Self::BinaryHeap => super::binary_heap::evaluate(tc),
            Self::Calculator => super::calculator::evaluate(tc),
            Self::ProductSequence(depth) | Self::Product(depth) => {
                let with_payload = matches!(self, Self::ProductSequence(_));
                let (factors, payload) = tc.draw(nested(depth, false, with_payload));
                let holds = if with_payload {
                    payload.len() < 24 || !payload.contains(&1)
                } else {
                    factors.iter().product::<i64>() < 24
                };
                observed(holds, || {
                    nested_repr(&factors, with_payload.then_some(&payload))
                })
            }
            Self::Sum => {
                let (factors, payload) = tc.draw(nested(4, true, true));
                let holds = payload.len() < 24 || !payload.contains(&1);
                observed(holds, || nested_repr(&factors, Some(&payload)))
            }
            Self::ModularMapping => {
                let value = tc.draw(
                    gs::integers::<i64>()
                        .min_value(0)
                        .max_value(1000)
                        .map(|n| (n * 37) % 1001),
                );
                observed(value < 900, || value.to_string())
            }
            Self::WeightedLinear => {
                let (x, y, z) = tc.draw(hegel::tuples!(
                    bounded(0, 20),
                    bounded(0, 20),
                    bounded(0, 20)
                ));
                observed(2 * x + y + z != 20, || format!("({x}, {y}, {z})"))
            }
            Self::Invoice | Self::InvoiceDerived => {
                let invoice = if matches!(self, Self::InvoiceDerived) {
                    tc.draw(gs::default::<Invoice>())
                } else {
                    tc.draw(invoices())
                };
                let holds = !invoice.is_valid() || invoice.total() == invoice.expected();
                observed(holds, || invoice.repr())
            }
            Self::FloatCancellation => {
                let (a, b) = tc.draw(hegel::tuples!(
                    gs::floats::<f64>().min_value(-1e6).max_value(1e6),
                    gs::floats::<f64>().min_value(-1e6).max_value(1e6),
                ));
                observed((a + b) - b == a, || format!("({a:?}, {b:?})"))
            }
            Self::ChunkedDecoder => {
                let transmission = tc.draw(transmissions());
                observed(transmission.holds(), || transmission.repr())
            }
            Self::HashCollision(modulus) => {
                let keys = || bounded(0, 10 * modulus - 1);
                let (entries, key, value) = tc.draw(hegel::tuples!(
                    gs::vecs(hegel::tuples!(keys(), bounded(0, 9))).max_size(20),
                    keys(),
                    bounded(0, 9),
                ));
                let mut map = HashMap::new(modulus);
                for &(key, value) in &entries {
                    map.put(key, value);
                }
                let others: std::collections::BTreeSet<_> = entries
                    .iter()
                    .map(|&(k, _)| k)
                    .filter(|&k| k != key)
                    .collect();
                let before: Vec<_> = others.iter().map(|&k| map.get(k)).collect();
                map.put(key, value);
                let after: Vec<_> = others.iter().map(|&k| map.get(k)).collect();
                observed(before == after, || format!("({entries:?}, {key}, {value})"))
            }
            Self::HashCollisionMachine(_) | Self::SnapshotStore => unreachable!("stateful runner"),
        }
    }
}

// Match the Hypothesis harness: render failing examples only.
fn observed(holds: bool, render: impl FnOnce() -> String) -> (String, bool) {
    (if holds { String::new() } else { render() }, holds)
}

pub fn bounded(min: i64, max: i64) -> gs::IntegerGenerator<i64> {
    gs::integers().min_value(min).max_value(max)
}

#[hegel::composite]
fn nested(tc: &TestCase, depth: usize, sum: bool, with_payload: bool) -> (Vec<i64>, Vec<i64>) {
    let mut factors = Vec::new();
    let mut upper = if sum { 100 } else { 10 };
    for _ in 0..depth {
        upper = tc.draw(bounded(1, upper));
        factors.push(upper);
    }
    let size = if sum {
        factors.iter().sum::<i64>()
    } else {
        factors.iter().product::<i64>()
    } as usize;
    let payload = if with_payload {
        tc.draw(gs::vecs(bounded(0, 1)).min_size(size).max_size(size))
    } else {
        Vec::new()
    };
    (factors, payload)
}

fn nested_repr(factors: &[i64], payload: Option<&Vec<i64>>) -> String {
    let mut fields: Vec<_> = factors.iter().map(ToString::to_string).collect();
    if let Some(payload) = payload {
        fields.push(format!("{payload:?}"));
    }
    format!("({})", fields.join(", "))
}

// Fully derived means no bounds, filtering, or customised field generators.
#[derive(Debug, hegel::DefaultGenerator, hegel::PrettyPrintable)]
struct Invoice {
    unit_price_cents: i64,
    quantity: i64,
    discount_percent: i64,
}

impl Invoice {
    fn is_valid(&self) -> bool {
        (1..=1000).contains(&self.unit_price_cents)
            && (1..=100).contains(&self.quantity)
            && (0..=50).contains(&self.discount_percent)
            && (self.unit_price_cents * self.quantity >= 1000 || self.discount_percent == 0)
    }
    fn total(&self) -> i64 {
        (self.unit_price_cents * (100 - self.discount_percent) / 100) * self.quantity
    }
    fn expected(&self) -> i64 {
        self.unit_price_cents * self.quantity * (100 - self.discount_percent) / 100
    }
    fn repr(&self) -> String {
        format!(
            "Invoice({}, {}, {})",
            self.unit_price_cents, self.quantity, self.discount_percent
        )
    }
}

#[hegel::composite]
fn invoices(tc: &TestCase) -> Invoice {
    let unit_price_cents = tc.draw(bounded(1, 1000));
    let quantity = tc.draw(bounded(1, 100));
    let discount_percent = if unit_price_cents * quantity >= 1000 {
        tc.draw(bounded(0, 50))
    } else {
        0
    };
    Invoice {
        unit_price_cents,
        quantity,
        discount_percent,
    }
}

#[derive(Debug, hegel::PrettyPrintable)]
enum Message {
    Binary(Vec<u8>),
    Text(String),
}

#[derive(Debug, hegel::PrettyPrintable)]
struct Transmission {
    message: Message,
    cuts: Vec<bool>,
}

#[hegel::composite]
fn transmissions(tc: &TestCase) -> Transmission {
    let message = tc.draw(gs::one_of([
        gs::binary().max_size(64).map(Message::Binary).boxed(),
        gs::text().max_size(16).map(Message::Text).boxed(),
    ]));
    let gaps = message.bytes().len().saturating_sub(1);
    let cuts = tc.draw(gs::vecs(gs::booleans()).min_size(gaps).max_size(gaps));
    Transmission { message, cuts }
}

impl Message {
    fn bytes(&self) -> &[u8] {
        match self {
            Self::Binary(bytes) => bytes,
            Self::Text(text) => text.as_bytes(),
        }
    }
}

impl Transmission {
    fn chunks(&self) -> Vec<&[u8]> {
        let bytes = self.message.bytes();
        if bytes.is_empty() {
            return Vec::new();
        }
        let mut chunks = Vec::new();
        let mut start = 0;
        for (index, &cut) in self.cuts.iter().enumerate() {
            if cut {
                chunks.push(&bytes[start..index + 1]);
                start = index + 1;
            }
        }
        chunks.push(&bytes[start..]);
        chunks
    }
    fn holds(&self) -> bool {
        match &self.message {
            Message::Binary(bytes) => self.chunks().concat() == *bytes,
            // Deliberate bug: each chunk is decoded independently.
            Message::Text(text) => {
                self.chunks()
                    .iter()
                    .map(|chunk| String::from_utf8_lossy(chunk))
                    .collect::<String>()
                    == *text
            }
        }
    }
    fn repr(&self) -> String {
        let sizes: Vec<_> = self.chunks().iter().map(|chunk| chunk.len()).collect();
        match &self.message {
            Message::Binary(bytes) => format!("(binary, {bytes:?}, {sizes:?})"),
            Message::Text(text) => format!("(text, {}, {sizes:?})", escaped(text)),
        }
    }
}

fn escaped(text: &str) -> String {
    let mut result = String::from("\"");
    for c in text.chars() {
        match c {
            '"' => result.push_str("\\\""),
            '\\' => result.push_str("\\\\"),
            ' '..='~' => result.push(c),
            _ => result.push_str(&format!("\\u{{{:x}}}", c as u32)),
        }
    }
    result.push('"');
    result
}

pub struct HashMap {
    modulus: i64,
    entries: Vec<(i64, i64)>,
}
impl HashMap {
    pub fn new(modulus: i64) -> Self {
        Self {
            modulus,
            entries: Vec::new(),
        }
    }
    pub fn put(&mut self, key: i64, value: i64) {
        // Deliberate bug: compare hashes instead of keys.
        if let Some(entry) = self
            .entries
            .iter_mut()
            .find(|(k, _)| k % self.modulus == key % self.modulus)
        {
            entry.1 = value;
        } else {
            self.entries.push((key, value));
        }
    }
    pub fn get(&self, key: i64) -> Option<i64> {
        self.entries
            .iter()
            .find(|(k, _)| k % self.modulus == key % self.modulus)
            .map(|(_, v)| *v)
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn invoice_rounds_at_the_wrong_stage() {
        let invoice = Invoice {
            unit_price_cents: 10,
            quantity: 100,
            discount_percent: 1,
        };
        assert!(invoice.is_valid());
        assert_eq!(invoice.total(), 900);
        assert_eq!(invoice.expected(), 990);
        let invalid = Invoice {
            unit_price_cents: i64::MAX,
            quantity: i64::MAX,
            discount_percent: i64::MIN,
        };
        assert!(!invalid.is_valid()); // No overflow while testing fully derived inputs.
    }
    #[test]
    fn decoder_fails_only_when_a_scalar_is_split() {
        let split = Transmission {
            message: Message::Text("\u{80}".into()),
            cuts: vec![true],
        };
        assert!(!split.holds());
        assert_eq!(split.repr(), "(text, \"\\u{80}\", [1, 1])");
        let whole = Transmission {
            message: Message::Text("\u{80}".into()),
            cuts: vec![false],
        };
        assert!(whole.holds());
        let binary = Transmission {
            message: Message::Binary(vec![0xc2, 0x80]),
            cuts: vec![true],
        };
        assert!(binary.holds());
        let empty = Transmission {
            message: Message::Text(String::new()),
            cuts: vec![],
        };
        assert!(empty.holds());
        assert!(empty.chunks().is_empty());
    }
    #[test]
    fn generators_preserve_dependent_domains() {
        hegel::Hegel::new(|tc: TestCase| {
            let (factors, payload) = tc.draw(nested(3, false, true));
            assert!(factors.iter().all(|&n| (1..=10).contains(&n)));
            assert!(factors.windows(2).all(|pair| pair[0] >= pair[1]));
            assert_eq!(payload.len(), factors.iter().product::<i64>() as usize);
            assert!(payload.iter().all(|&n| n == 0 || n == 1));
            let (factors, payload) = tc.draw(nested(4, true, true));
            assert!(factors.windows(2).all(|pair| pair[0] >= pair[1]));
            assert_eq!(payload.len(), factors.iter().sum::<i64>() as usize);
            let invoice = tc.draw(invoices());
            assert!(invoice.is_valid());
            if invoice.unit_price_cents * invoice.quantity < 1000 {
                assert_eq!(invoice.discount_percent, 0);
            }
            let transmission = tc.draw(transmissions());
            assert_eq!(
                transmission.cuts.len(),
                transmission.message.bytes().len().saturating_sub(1)
            );
            match transmission.message {
                Message::Binary(bytes) => assert!(bytes.len() <= 64),
                Message::Text(text) => assert!(text.chars().count() <= 16),
            }
        })
        .settings(
            hegel::Settings::from_profile("base")
                .seed(Some(42))
                .database(None)
                .test_cases(50)
                .phases([hegel::Phase::Generate])
                .suppress_health_check(hegel::HealthCheck::all()),
        )
        .run();
    }
    #[test]
    fn hash_collision_overwrites_another_key() {
        let mut map = HashMap::new(10);
        map.put(0, 0);
        map.put(10, 1);
        assert_eq!(map.get(0), Some(1));
        map.put(1, 2);
        assert_eq!(map.get(0), Some(1));
        assert_eq!(map.get(1), Some(2));
    }
}

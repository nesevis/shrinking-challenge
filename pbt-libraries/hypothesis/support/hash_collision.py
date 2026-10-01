from hypothesis import given, strategies as st


# One fixture for every hash modulus: keys are drawn from range(10 * modulus), so collisions are distinct keys congruent mod modulus.
class HashMap:
    def __init__(self, modulus):
        self.modulus = modulus
        self.entries = []

    def hash(self, key):
        return key % self.modulus

    # Deliberate bug: put and get match entries by hash code rather than by key, so a key overwrites and reads any key sharing its hash.
    def put(self, key, value):
        for entry in self.entries:
            if self.hash(entry[0]) == self.hash(key):
                entry[1] = value
                return
        self.entries.append([key, value])

    def get(self, key):
        for entry_key, entry_value in self.entries:
            if self.hash(entry_key) == self.hash(key):
                return entry_value
        return None


def make_test(modulus):
    keys = st.integers(0, 10 * modulus - 1)
    values = st.integers(0, 9)
    strategy = st.tuples(st.lists(st.tuples(keys, values), max_size=20), keys, values)

    # Frame property: putting a key leaves every other key in the map unchanged.
    @given(strategy)
    def test(value):
        entries, key, new_value = value
        hash_map = HashMap(modulus)
        for entry_key, entry_value in entries:
            hash_map.put(entry_key, entry_value)
        other_keys = sorted({entry_key for entry_key, _ in entries} - {key})
        before = [hash_map.get(other) for other in other_keys]
        hash_map.put(key, new_value)
        assert [hash_map.get(other) for other in other_keys] == before

    return test


# The machine most recently created; the harness records a run straight after it finishes.
latest_machine = None


# The same frame property as a state machine, checked after every put.
def make_state_machine_test(modulus):
    from hypothesis.stateful import RuleBasedStateMachine, get_state_machine_test, rule

    keys = st.integers(0, 10 * modulus - 1)
    values = st.integers(0, 9)

    class HashCollisionMachine(RuleBasedStateMachine):
        def __init__(self):
            super().__init__()
            global latest_machine
            latest_machine = self
            self.hash_map = HashMap(modulus)
            self.keys = set()
            self.steps = []

        @rule(key=keys, value=values)
        def put(self, key, value):
            self.steps.append(f"put({key}, {value})")
            other_keys = sorted(self.keys - {key})
            before = [self.hash_map.get(other) for other in other_keys]
            self.hash_map.put(key, value)
            self.keys.add(key)
            assert [self.hash_map.get(other) for other in other_keys] == before

    test = get_state_machine_test(HashCollisionMachine)
    # get_state_machine_test applies its own settings; clear the marker so the harness can apply its settings.
    del test._hypothesis_internal_settings_applied
    return test


# The test's only argument is `data`, whose repr says nothing about the run, so describe the steps the machine ran instead.
def describe(kwargs):
    return {"steps": "[" + ", ".join(latest_machine.steps) + "]"}

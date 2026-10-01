from hypothesis import strategies as st
from hypothesis.stateful import (
    Bundle,
    RuleBasedStateMachine,
    consumes,
    get_state_machine_test,
    rule,
)


# A versioned key-value store. A snapshot sees the store as it was when the snapshot was taken, until it is released.
# Compaction may discard any version no live snapshot can see.
class SnapshotStore:
    def __init__(self):
        self.versions = {}
        self.live_snapshots = {}
        self.clock = 0
        self.next_snapshot_id = 0

    def put(self, key, value):
        self.clock += 1
        self.versions.setdefault(key, []).append((self.clock, value))

    def get(self, key):
        versions = self.versions.get(key)
        return versions[-1][1] if versions else None

    def snapshot(self):
        handle = (self.next_snapshot_id, self.clock)
        self.live_snapshots[self.next_snapshot_id] = self.clock
        self.next_snapshot_id += 1
        return handle

    def read(self, handle, key):
        _, timestamp = handle
        visible = [value for stamp, value in self.versions.get(key, []) if stamp <= timestamp]
        return visible[-1] if visible else None

    def release(self, handle):
        snapshot_id, _ = handle
        del self.live_snapshots[snapshot_id]

    def compact(self):
        # Deliberate bug: keeps history back to the newest live snapshot rather than the oldest.
        horizon = max(self.live_snapshots.values(), default=self.clock)
        for key, versions in self.versions.items():
            floors = [i for i, (stamp, _) in enumerate(versions) if stamp <= horizon]
            if floors:
                self.versions[key] = versions[floors[-1]:]


class Snapshot:
    def __init__(self, name, handle, visible_writes):
        self.name = name
        self.handle = handle
        self.visible_writes = visible_writes


keys = st.integers(0, 9)
values = st.integers(0, 9)


# The model never compacts: it keeps every write in order, and a snapshot remembers how many writes it can see.
class SnapshotStoreMachine(RuleBasedStateMachine):
    snapshots = Bundle("snapshots")

    def __init__(self):
        super().__init__()
        global latest_machine
        latest_machine = self
        self.writes = []
        self.store = SnapshotStore()
        self.created = 0
        # The steps that ran, naming snapshots s0, s1, … in creation order, as the Exhaust renderer does.
        self.steps = []

    def latest(self, key, visible_writes):
        matching = [value for k, value in self.writes[:visible_writes] if k == key]
        return matching[-1] if matching else None

    @rule(key=keys, value=values)
    def put(self, key, value):
        self.steps.append(f"put({key}, {value})")
        self.writes.append((key, value))
        self.store.put(key, value)

    @rule(key=keys)
    def get(self, key):
        self.steps.append(f"get({key})")
        assert self.store.get(key) == self.latest(key, len(self.writes))

    @rule(target=snapshots)
    def snapshot(self):
        name = f"s{self.created}"
        self.created += 1
        self.steps.append(f"{name} = snapshot()")
        return Snapshot(name, self.store.snapshot(), len(self.writes))

    @rule(snapshot=snapshots, key=keys)
    def read(self, snapshot, key):
        self.steps.append(f"read({snapshot.name}, {key})")
        assert self.store.read(snapshot.handle, key) == self.latest(key, snapshot.visible_writes)

    @rule(snapshot=consumes(snapshots))
    def release(self, snapshot):
        self.steps.append(f"release({snapshot.name})")
        self.store.release(snapshot.handle)

    @rule()
    def compact(self):
        self.steps.append("compact()")
        self.store.compact()


# The machine most recently created; the harness records a run straight after it finishes.
latest_machine = None


# The test's only argument is `data`, whose repr says nothing about the run, so describe the steps the machine ran instead.
def describe(kwargs):
    return {"steps": "[" + ", ".join(latest_machine.steps) + "]"}


test = get_state_machine_test(SnapshotStoreMachine)
# get_state_machine_test applies its own settings; clear the marker so the harness can apply its settings.
del test._hypothesis_internal_settings_applied

use crate::challenges::{Challenge, HashMap, bounded};
use hegel::TestCase;
use hegel::stateful::{self, Pool};
use std::cell::RefCell;
use std::collections::{BTreeMap, BTreeSet};
use std::panic::{AssertUnwindSafe, catch_unwind, panic_any, resume_unwind};
use std::rc::Rc;

#[derive(Debug)]
struct PropertyFailure;
fn check(holds: bool) {
    if !holds {
        panic_any(PropertyFailure);
    }
}

type Trace = Rc<RefCell<Vec<String>>>;

// Only our property-failure marker becomes a recorded failure. Rejected or
// overrun histories unwind with Hegel's own control payload and are not CEs.
pub fn evaluate(challenge: Challenge, tc: TestCase) -> (String, bool) {
    let trace = Trace::default();
    let result = catch_unwind(AssertUnwindSafe(|| match challenge {
        Challenge::HashCollisionMachine(modulus) => {
            let map = HashCollisionMachine {
                map: HashMap::new(modulus),
                modulus,
                keys: BTreeSet::new(),
                trace: trace.clone(),
            };
            stateful::machine(map).steps(50).run(tc);
        }
        Challenge::SnapshotStore => {
            let snapshots = stateful::pool(&tc);
            let machine = SnapshotStoreMachine {
                store: SnapshotStore::default(),
                writes: Vec::new(),
                snapshots,
                trace: trace.clone(),
            };
            stateful::machine(machine).steps(50).run(tc);
        }
        _ => unreachable!("generator runner"),
    }));
    let holds = match result {
        Ok(()) => true,
        Err(payload) if payload.is::<PropertyFailure>() => false,
        Err(payload) => resume_unwind(payload),
    };
    let repr = if holds {
        String::new()
    } else {
        format!("[{}]", trace.borrow().join(", "))
    };
    (repr, holds)
}

struct HashCollisionMachine {
    map: HashMap,
    modulus: i64,
    keys: BTreeSet<i64>,
    trace: Trace,
}

#[hegel::state_machine]
impl HashCollisionMachine {
    #[rule]
    fn put(&mut self, tc: TestCase) {
        let key = tc.draw(bounded(0, 10 * self.modulus - 1));
        let value = tc.draw(bounded(0, 9));
        self.trace.borrow_mut().push(format!("put({key}, {value})"));
        let others: Vec<_> = self.keys.iter().copied().filter(|&k| k != key).collect();
        let before: Vec<_> = others.iter().map(|&k| self.map.get(k)).collect();
        self.map.put(key, value);
        self.keys.insert(key);
        let after: Vec<_> = others.iter().map(|&k| self.map.get(k)).collect();
        check(before == after);
    }
}

#[derive(Default)]
struct SnapshotStore {
    versions: BTreeMap<i64, Vec<(usize, i64)>>,
    live_snapshots: BTreeMap<usize, usize>,
    clock: usize,
    next_snapshot_id: usize,
}
impl SnapshotStore {
    fn put(&mut self, key: i64, value: i64) {
        self.clock += 1;
        self.versions
            .entry(key)
            .or_default()
            .push((self.clock, value));
    }
    fn get(&self, key: i64) -> Option<i64> {
        self.versions.get(&key)?.last().map(|&(_, value)| value)
    }
    fn snapshot(&mut self) -> (usize, usize) {
        let handle = (self.next_snapshot_id, self.clock);
        self.live_snapshots.insert(handle.0, handle.1);
        self.next_snapshot_id += 1;
        handle
    }
    fn read(&self, handle: (usize, usize), key: i64) -> Option<i64> {
        self.versions
            .get(&key)?
            .iter()
            .rev()
            .find(|&&(stamp, _)| stamp <= handle.1)
            .map(|&(_, value)| value)
    }
    fn release(&mut self, handle: (usize, usize)) {
        self.live_snapshots
            .remove(&handle.0)
            .expect("live snapshot");
    }
    fn compact(&mut self) {
        // Deliberate bug: newest live snapshot rather than oldest.
        let horizon = self
            .live_snapshots
            .values()
            .copied()
            .max()
            .unwrap_or(self.clock);
        for versions in self.versions.values_mut() {
            if let Some(floor) = versions.iter().rposition(|&(stamp, _)| stamp <= horizon) {
                versions.drain(..floor);
            }
        }
    }
}

#[derive(Clone, Debug, hegel::PrettyPrintable)]
struct Snapshot {
    handle: (usize, usize),
    visible_writes: usize,
}

struct SnapshotStoreMachine {
    store: SnapshotStore,
    writes: Vec<(i64, i64)>,
    snapshots: Pool<Snapshot>,
    trace: Trace,
}
impl SnapshotStoreMachine {
    fn latest(&self, key: i64, visible_writes: usize) -> Option<i64> {
        self.writes[..visible_writes]
            .iter()
            .rev()
            .find(|&&(k, _)| k == key)
            .map(|&(_, value)| value)
    }
}

#[hegel::state_machine]
impl SnapshotStoreMachine {
    #[rule]
    fn put(&mut self, tc: TestCase) {
        let key = tc.draw(bounded(0, 9));
        let value = tc.draw(bounded(0, 9));
        self.trace.borrow_mut().push(format!("put({key}, {value})"));
        self.writes.push((key, value));
        self.store.put(key, value);
    }
    #[rule]
    fn get(&mut self, tc: TestCase) {
        let key = tc.draw(bounded(0, 9));
        self.trace.borrow_mut().push(format!("get({key})"));
        check(self.store.get(key) == self.latest(key, self.writes.len()));
    }
    #[rule]
    fn snapshot(&mut self, _: TestCase) {
        let handle = self.store.snapshot();
        self.trace
            .borrow_mut()
            .push(format!("s{} = snapshot()", handle.0));
        self.snapshots.add(Snapshot {
            handle,
            visible_writes: self.writes.len(),
        });
    }
    #[rule]
    fn read(&mut self, tc: TestCase) {
        let snapshot = tc.draw(self.snapshots.values_reusable()).clone();
        let key = tc.draw(bounded(0, 9));
        self.trace
            .borrow_mut()
            .push(format!("read(s{}, {key})", snapshot.handle.0));
        check(self.store.read(snapshot.handle, key) == self.latest(key, snapshot.visible_writes));
    }
    #[rule]
    fn release(&mut self, tc: TestCase) {
        let snapshot = tc.draw(self.snapshots.values_consumed());
        self.trace
            .borrow_mut()
            .push(format!("release(s{})", snapshot.handle.0));
        self.store.release(snapshot.handle);
    }
    #[rule]
    fn compact(&mut self, _: TestCase) {
        self.trace.borrow_mut().push("compact()".into());
        self.store.compact();
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn compaction_breaks_an_older_live_snapshot() {
        let mut store = SnapshotStore::default();
        store.put(0, 0);
        let old = store.snapshot();
        store.put(0, 0);
        let new = store.snapshot();
        assert_eq!(store.read(old, 0), Some(0));
        store.compact();
        assert_eq!(store.read(old, 0), None);
        assert_eq!(store.read(new, 0), Some(0));
        assert_eq!(store.get(0), Some(0));
        store.release(new);
        assert_eq!(store.live_snapshots.len(), 1);
    }
    #[test]
    fn compaction_without_snapshots_keeps_current_values() {
        let mut store = SnapshotStore::default();
        store.put(0, 1);
        store.put(0, 2);
        store.put(1, 3);
        store.compact();
        assert_eq!(store.get(0), Some(2));
        assert_eq!(store.get(1), Some(3));
        assert_eq!(store.get(2), None);
    }
}

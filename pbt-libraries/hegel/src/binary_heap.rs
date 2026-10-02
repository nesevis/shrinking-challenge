//! Port of the wrong binary heap challenge, matching Exhaust's generator and traversal.

use hegel::TestCase;
use hegel::generators as gs;

#[derive(Clone, Debug, PartialEq, Eq, hegel::PrettyPrintable)]
enum Heap {
    Empty,
    Node(i64, Box<Heap>, Box<Heap>),
}

impl Heap {
    fn repr(&self) -> String {
        match self {
            Self::Empty => "None".into(),
            Self::Node(key, left, right) => {
                format!("({key}, {}, {})", left.repr(), right.repr())
            }
        }
    }

    fn is_valid(&self, minimum: i64) -> bool {
        match self {
            Self::Empty => true,
            Self::Node(key, left, right) => {
                *key >= minimum && left.is_valid(*key) && right.is_valid(*key)
            }
        }
    }

    fn to_list(&self) -> Vec<i64> {
        let mut stack = vec![self];
        let mut result = Vec::new();
        while let Some(heap) = stack.pop() {
            if let Self::Node(key, left, right) = heap {
                result.push(*key);
                stack.push(left);
                stack.push(right);
            }
        }
        result
    }

    fn wrong_to_sorted_list(&self) -> Vec<i64> {
        match self {
            Self::Empty => Vec::new(),
            Self::Node(key, left, right) => {
                let mut result = vec![*key];
                // Deliberate bug: traverse once rather than repeatedly extract the minimum.
                result.extend(merge(left, right).to_list());
                result
            }
        }
    }

    fn holds(&self) -> bool {
        if !self.is_valid(0) {
            return true;
        }
        let actual = self.wrong_to_sorted_list();
        let mut ordered = actual.clone();
        ordered.sort_unstable();
        let mut reference = self.to_list();
        reference.sort_unstable();
        reference == ordered && actual == ordered
    }
}

fn merge(first: &Heap, second: &Heap) -> Heap {
    match (first, second) {
        (_, Heap::Empty) => first.clone(),
        (Heap::Empty, _) => second.clone(),
        (Heap::Node(x, left_x, right_x), Heap::Node(y, left_y, right_y)) => {
            if x <= y {
                Heap::Node(*x, Box::new(merge(right_x, second)), left_x.clone())
            } else {
                Heap::Node(*y, Box::new(merge(right_y, first)), left_y.clone())
            }
        }
    }
}

#[hegel::composite]
fn heaps(tc: &TestCase) -> Heap {
    let depth = tc.draw(super::challenges::bounded(0, 20));
    tc.draw(build(0, depth))
}

#[hegel::composite]
fn build(tc: &TestCase, minimum: i64, depth: i64) -> Heap {
    if depth == 0 {
        return Heap::Empty;
    }
    // Hegel has no weighted one_of; five equivalent node alternatives retain
    // one_of's span structure and the original 1:5 empty/node multiplicity.
    tc.draw(hegel::one_of!(
        gs::just(Heap::Empty),
        nodes(minimum, depth),
        nodes(minimum, depth),
        nodes(minimum, depth),
        nodes(minimum, depth),
        nodes(minimum, depth),
    ))
}

#[hegel::composite]
fn nodes(tc: &TestCase, minimum: i64, depth: i64) -> Heap {
    let key = tc.draw(super::challenges::bounded(minimum, i64::MAX));
    let left = tc.draw(build(key, depth / 2));
    let right = tc.draw(build(key, depth / 2));
    Heap::Node(key, Box::new(left), Box::new(right))
}

pub(crate) fn evaluate(tc: &TestCase) -> (String, bool) {
    let heap = tc.draw(heaps());
    let holds = heap.holds();
    (if holds { String::new() } else { heap.repr() }, holds)
}

#[cfg(test)]
mod tests {
    use super::*;

    fn node(key: i64, left: Heap, right: Heap) -> Heap {
        Heap::Node(key, Box::new(left), Box::new(right))
    }

    #[test]
    fn known_four_node_failure_preserves_values_but_not_order() {
        let heap = node(
            0,
            Heap::Empty,
            node(
                0,
                node(0, Heap::Empty, Heap::Empty),
                node(1, Heap::Empty, Heap::Empty),
            ),
        );
        assert!(heap.is_valid(0));
        assert_eq!(
            heap.repr(),
            "(0, None, (0, (0, None, None), (1, None, None)))"
        );
        assert_eq!(heap.wrong_to_sorted_list(), [0, 0, 1, 0]);
        assert!(!heap.holds());
        assert!(Heap::Empty.holds());
        assert!(node(0, Heap::Empty, node(1, Heap::Empty, Heap::Empty)).holds());
    }

    #[test]
    fn generated_heaps_obey_depth_and_key_constraints() {
        hegel::Hegel::new(|tc: TestCase| {
            assert_eq!(tc.draw(build(0, 0)), Heap::Empty);
            let heap = tc.draw(heaps());
            assert!(heap.is_valid(0));
            assert!(heap.to_list().len() <= 31);
            // Exercise the full dependent key boundary without arithmetic overflow.
            let heap = tc.draw(build(i64::MAX, 20));
            assert!(heap.to_list().iter().all(|&key| key == i64::MAX));
            assert!(heap.holds());
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
}

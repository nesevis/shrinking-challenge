use std::collections::HashSet;

use hegel::TestCase;
use hegel::generators::{self as gs, PrintableGenerator};

pub fn arrays(minimum: usize, maximum: usize) -> impl PrintableGenerator<Vec<i64>> {
    gs::vecs(gs::integers::<i64>())
        .min_size(minimum)
        .max_size(maximum)
}

pub fn passes(values: &[i64]) -> bool {
    (values.iter().collect::<HashSet<_>>().len() == values.len() && {
        let mut sorted = values.to_vec();
        sorted.sort_unstable();
        values == sorted
    }) == false
}

pub(crate) fn evaluate(tc: &TestCase) -> (String, bool) {
    let values = tc.draw(arrays(5, 10));
    let holds = passes(&values);
    (
        if holds {
            String::new()
        } else {
            format!("{values:?}")
        },
        holds,
    )
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn ascending_array_property_fails_for_sorted_unique_values() {
        for values in [
            vec![-2, -1, 0, 1, 2],
            vec![0, 1, 2, 3, 4],
            (-5..5).collect(),
        ] {
            assert!(!passes(&values));
        }
        for values in [vec![0; 5], vec![0, 1, 2, 3, 4, 3]] {
            assert!(passes(&values));
        }
    }
}

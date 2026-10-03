//! Refund allocation incorrectly includes non-refundable processing fees in its weights.

use hegel::TestCase;
use hegel::generators::{self as gs, Generator};

const PROCESSING_FEE_CENTS: i64 = 30;
const CHARGE_LIMIT: usize = 20;

#[derive(Clone, Debug, hegel::DefaultGenerator, hegel::PrettyPrintable)]
struct Charge {
    paid_cents: i64,
}

impl Charge {
    fn refundable_cents(&self) -> i128 {
        i128::from(self.paid_cents) - i128::from(PROCESSING_FEE_CENTS)
    }
}

#[derive(Clone, Debug, hegel::DefaultGenerator, hegel::PrettyPrintable)]
struct RefundRequest {
    charges: Vec<Charge>,
    refund_cents: i64,
}

impl RefundRequest {
    fn total_refundable(&self) -> i128 {
        self.charges.iter().map(Charge::refundable_cents).sum()
    }

    fn is_valid(&self) -> bool {
        (1..=CHARGE_LIMIT).contains(&self.charges.len())
            && self
                .charges
                .iter()
                .all(|charge| charge.paid_cents > PROCESSING_FEE_CENTS)
            && self.refund_cents >= 0
            && i128::from(self.refund_cents) <= self.total_refundable()
    }

    fn repr(&self) -> String {
        let payments: Vec<_> = self
            .charges
            .iter()
            .map(|charge| charge.paid_cents)
            .collect();
        format!("RefundRequest({payments:?}, {})", self.refund_cents)
    }

    fn satisfies_contract(&self, allocations: &[i64]) -> bool {
        if !self.is_valid() || allocations.len() != self.charges.len() {
            return false;
        }
        let total = self.total_refundable();
        let refund = i128::from(self.refund_cents);
        if allocations
            .iter()
            .map(|amount| i128::from(*amount))
            .sum::<i128>()
            != refund
        {
            return false;
        }

        let mut remainders = Vec::new();
        let mut rounded_up = Vec::new();
        for (charge, allocation) in self.charges.iter().zip(allocations) {
            let actual = i128::from(*allocation);
            if actual < 0 || actual > charge.refundable_cents() {
                return false;
            }
            let numerator = refund * charge.refundable_cents();
            let floor = numerator / total;
            let remainder = numerator % total;
            let ceiling = floor + i128::from(remainder != 0);
            if actual != floor && actual != ceiling {
                return false;
            }
            remainders.push(remainder);
            rounded_up.push(actual > floor);
        }

        for recipient in 0..allocations.len() {
            if !rounded_up[recipient] {
                continue;
            }
            for other in 0..allocations.len() {
                if !rounded_up[other]
                    && (remainders[other] > remainders[recipient]
                        || (remainders[other] == remainders[recipient] && other < recipient))
                {
                    return false;
                }
            }
        }
        true
    }

    fn allocate_refund(&self) -> Vec<i64> {
        // Deliberate bug, matching Exhaust: use gross payments instead of net balances.
        let total: i128 = self
            .charges
            .iter()
            .map(|charge| i128::from(charge.paid_cents))
            .sum();
        let numerators: Vec<_> = self
            .charges
            .iter()
            .map(|charge| i128::from(self.refund_cents) * i128::from(charge.paid_cents))
            .collect();
        let mut allocations: Vec<_> = numerators
            .iter()
            .map(|numerator| (numerator / total) as i64)
            .collect();
        let allocated: i128 = allocations.iter().map(|amount| i128::from(*amount)).sum();
        let remaining = (i128::from(self.refund_cents) - allocated) as usize;
        let mut priority: Vec<_> = (0..numerators.len()).collect();
        priority.sort_by(|left, right| {
            (numerators[*right] % total)
                .cmp(&(numerators[*left] % total))
                .then_with(|| left.cmp(right))
        });
        for index in priority.into_iter().take(remaining) {
            allocations[index] += 1;
        }
        allocations
    }
}

#[hegel::composite]
fn requests(tc: &TestCase) -> RefundRequest {
    let charges = tc.draw(
        gs::vecs(
            gs::integers::<i64>()
                .min_value(PROCESSING_FEE_CENTS + 1)
                .map(|paid_cents| Charge { paid_cents }),
        )
        .min_size(1)
        .max_size(CHARGE_LIMIT),
    );
    let total: i128 = charges.iter().map(Charge::refundable_cents).sum();
    let refund_cents = tc.draw(
        gs::integers::<i64>()
            .min_value(0)
            .max_value(total.min(i128::from(i64::MAX)) as i64),
    );
    RefundRequest {
        charges,
        refund_cents,
    }
}

pub(crate) fn evaluate(tc: &TestCase, derived: bool) -> (String, bool) {
    let request = if derived {
        // Raw derivation: no field overrides, filtering, or request repair.
        tc.draw(gs::default::<RefundRequest>())
    } else {
        tc.draw(requests())
    };
    tc.assume(request.is_valid());
    let holds = request.satisfies_contract(&request.allocate_refund());
    (if holds { String::new() } else { request.repr() }, holds)
}

#[cfg(test)]
mod tests {
    use super::*;

    fn request(payments: &[i64], refund_cents: i64) -> RefundRequest {
        RefundRequest {
            charges: payments
                .iter()
                .map(|paid_cents| Charge {
                    paid_cents: *paid_cents,
                })
                .collect(),
            refund_cents,
        }
    }

    fn repaired_allocations(request: &RefundRequest) -> Vec<i64> {
        let total = request.total_refundable();
        let numerators: Vec<_> = request
            .charges
            .iter()
            .map(|charge| i128::from(request.refund_cents) * charge.refundable_cents())
            .collect();
        let mut allocations: Vec<_> = numerators
            .iter()
            .map(|numerator| (numerator / total) as i64)
            .collect();
        let allocated: i128 = allocations.iter().map(|amount| i128::from(*amount)).sum();
        let remaining = (i128::from(request.refund_cents) - allocated) as usize;
        let mut priority: Vec<_> = (0..numerators.len()).collect();
        priority.sort_by(|left, right| {
            (numerators[*right] % total)
                .cmp(&(numerators[*left] % total))
                .then_with(|| left.cmp(right))
        });
        for index in priority.into_iter().take(remaining) {
            allocations[index] += 1;
        }
        allocations
    }

    #[test]
    fn fee_imbalance_matches_exhaust_and_conservation_alone_cannot_detect_it() {
        let input = request(&[31, 33], 4);
        assert!(input.is_valid());
        assert_eq!(input.repr(), "RefundRequest([31, 33], 4)");
        assert_eq!(input.allocate_refund(), [2, 2]);
        assert!(!input.satisfies_contract(&[2, 2]));
        assert!(input.satisfies_contract(&[1, 3]));
        for input in [
            request(&[31, 34], 2),
            request(&[33, 31], 2),
            request(&[31, 31, 33], 3),
        ] {
            let allocations = input.allocate_refund();
            assert_eq!(allocations.iter().sum::<i64>(), input.refund_cents);
            assert!(!input.satisfies_contract(&allocations));
            assert!(input.satisfies_contract(&repaired_allocations(&input)));
        }
    }

    #[test]
    fn smaller_valid_requests_pass_and_ties_follow_input_order() {
        for input in [
            request(&[31, 31], 1),
            request(&[31], 1),
            request(&[31, 33], 0),
        ] {
            assert!(input.satisfies_contract(&input.allocate_refund()));
        }
        let equal = request(&[31, 31], 1);
        assert!(equal.satisfies_contract(&[1, 0]));
        assert!(!equal.satisfies_contract(&[0, 1]));
        let unequal = request(&[32, 31], 1);
        assert!(unequal.satisfies_contract(&[1, 0]));
        assert!(!unequal.satisfies_contract(&[0, 1]));
        assert!(!equal.satisfies_contract(&[1]));
        assert!(!equal.satisfies_contract(&[0, 0]));
        assert!(!equal.satisfies_contract(&[-1, 2]));
    }

    #[test]
    fn domain_boundaries_and_widened_arithmetic_are_safe() {
        for input in [
            request(&[], 0),
            request(&[30], 0),
            request(&[i64::MIN], 0),
            request(&[31], -1),
            request(&[31], 2),
            request(&[31; 21], 0),
        ] {
            assert!(!input.is_valid());
            assert!(!input.satisfies_contract(&[]));
        }
        let single = request(&[i64::MAX], i64::MAX - PROCESSING_FEE_CENTS);
        assert!(single.satisfies_contract(&single.allocate_refund()));
        let large = request(&[i64::MAX; CHARGE_LIMIT], i64::MAX);
        assert!(large.total_refundable() > i128::from(i64::MAX));
        assert!(large.satisfies_contract(&large.allocate_refund()));
        assert!(large.satisfies_contract(&repaired_allocations(&large)));
    }

    #[test]
    fn constructive_generation_and_repaired_allocator_obey_the_contract() {
        hegel::Hegel::new(|tc: TestCase| {
            let input = tc.draw(requests());
            assert!(input.is_valid());
            assert!(input.satisfies_contract(&repaired_allocations(&input)));
            let allocations = input.allocate_refund();
            assert_eq!(
                allocations
                    .iter()
                    .map(|amount| i128::from(*amount))
                    .sum::<i128>(),
                i128::from(input.refund_cents)
            );
        })
        .settings(
            hegel::Settings::from_profile("base")
                .seed(Some(42))
                .database(None)
                .test_cases(2000)
                .phases([hegel::Phase::Generate])
                .suppress_health_check(hegel::HealthCheck::all()),
        )
        .run();
    }

    #[test]
    fn raw_derivation_constructs_nested_charges_and_accepts_valid_requests() {
        let mut valid = 0;
        let mut invalid = 0;
        hegel::Hegel::new(|tc: TestCase| {
            let input = tc.draw(gs::default::<RefundRequest>());
            if input.is_valid() {
                valid += 1;
                assert!(input.satisfies_contract(&repaired_allocations(&input)));
            } else {
                invalid += 1;
            }
        })
        .settings(
            hegel::Settings::from_profile("base")
                .seed(Some(42))
                .database(None)
                .test_cases(2000)
                .phases([hegel::Phase::Generate])
                .suppress_health_check(hegel::HealthCheck::all()),
        )
        .run();
        assert!(valid > 0);
        assert!(invalid > 0);
    }
}

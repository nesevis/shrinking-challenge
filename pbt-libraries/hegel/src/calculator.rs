//! Calculator challenge: a nonliteral denominator can still evaluate to zero.

use hegel::TestCase;
use hegel::generators::{self as gs, Generator, PrintableGenerator};

#[derive(Clone, Debug, hegel::PrettyPrintable)]
enum Expr {
    Value(i64),
    Add(Box<Expr>, Box<Expr>),
    Div(Box<Expr>, Box<Expr>),
}

#[derive(Debug, PartialEq, Eq)]
enum EvalError {
    DivisionByZero,
}

impl Expr {
    fn repr(&self) -> String {
        match self {
            Self::Value(value) => value.to_string(),
            Self::Add(left, right) => format!("('+', {}, {})", left.repr(), right.repr()),
            Self::Div(left, right) => format!("('/', {}, {})", left.repr(), right.repr()),
        }
    }

    fn contains_literal_division_by_zero(&self) -> bool {
        match self {
            Self::Value(_) => false,
            Self::Div(_, right) if matches!(right.as_ref(), Self::Value(0)) => true,
            Self::Add(left, right) | Self::Div(left, right) => {
                left.contains_literal_division_by_zero()
                    || right.contains_literal_division_by_zero()
            }
        }
    }

    fn eval(&self) -> Result<i128, EvalError> {
        // At depth <= 5 there are at most 32 i64 leaves, so exact sums fit i128.
        // Widening also makes i64::MIN / -1 valid rather than an overflow failure.
        match self {
            Self::Value(value) => Ok(i128::from(*value)),
            Self::Add(left, right) => Ok(left.eval()? + right.eval()?),
            Self::Div(left, right) => {
                let numerator = left.eval()?;
                let denominator = right.eval()?;
                if denominator == 0 {
                    return Err(EvalError::DivisionByZero);
                }
                // Python // rounds toward negative infinity, not toward zero.
                let quotient = numerator / denominator;
                let remainder = numerator % denominator;
                Ok(if remainder != 0 && (numerator < 0) != (denominator < 0) {
                    quotient - 1
                } else {
                    quotient
                })
            }
        }
    }
}

fn expressions() -> impl PrintableGenerator<Expr> {
    gs::recursive(gs::integers::<i64>().map(Expr::Value), |subtrees| {
        hegel::one_of!(
            hegel::tuples!(subtrees.clone(), subtrees.clone())
                .map(|(left, right)| Expr::Add(Box::new(left), Box::new(right))),
            hegel::tuples!(subtrees.clone(), subtrees)
                .map(|(left, right)| Expr::Div(Box::new(left), Box::new(right))),
        )
    })
    .max_depth(5)
    .max_leaves(32)
}

pub(crate) fn evaluate(tc: &TestCase) -> (String, bool) {
    let expression = tc.draw(expressions());
    // Match Hypothesis's assumption: reject every literal x / 0, including nested ones.
    tc.assume(!expression.contains_literal_division_by_zero());
    let holds = expression.eval().is_ok();
    (
        if holds {
            String::new()
        } else {
            expression.repr()
        },
        holds,
    )
}

#[cfg(test)]
mod tests {
    use super::*;

    fn add(left: Expr, right: Expr) -> Expr {
        Expr::Add(Box::new(left), Box::new(right))
    }

    fn div(left: Expr, right: Expr) -> Expr {
        Expr::Div(Box::new(left), Box::new(right))
    }

    #[test]
    fn computed_zero_divisor_passes_the_literal_precondition_but_fails_evaluation() {
        let expression = div(Expr::Value(0), add(Expr::Value(0), Expr::Value(0)));
        assert!(!expression.contains_literal_division_by_zero());
        assert_eq!(expression.eval(), Err(EvalError::DivisionByZero));
        assert_eq!(expression.repr(), "('/', 0, ('+', 0, 0))");
        let cancellation = div(Expr::Value(1), add(Expr::Value(3), Expr::Value(-3)));
        assert!(!cancellation.contains_literal_division_by_zero());
        assert_eq!(cancellation.eval(), Err(EvalError::DivisionByZero));
        let quotient_zero = div(Expr::Value(1), div(Expr::Value(1), Expr::Value(2)));
        assert!(!quotient_zero.contains_literal_division_by_zero());
        assert_eq!(quotient_zero.eval(), Err(EvalError::DivisionByZero));
    }

    #[test]
    fn precondition_detects_literal_zero_divisors_in_both_subtrees() {
        let literal = div(Expr::Value(1), Expr::Value(0));
        assert!(literal.contains_literal_division_by_zero());
        assert!(add(literal.clone(), Expr::Value(2)).contains_literal_division_by_zero());
        assert!(div(Expr::Value(2), literal).contains_literal_division_by_zero());
        assert!(!Expr::Value(0).contains_literal_division_by_zero());
    }

    #[test]
    fn evaluation_matches_floor_division_and_avoids_machine_integer_overflow() {
        for (numerator, denominator, expected) in [(7, 3, 2), (-7, 3, -3), (7, -3, -3), (-7, -3, 2)]
        {
            assert_eq!(
                div(Expr::Value(numerator), Expr::Value(denominator)).eval(),
                Ok(expected)
            );
        }
        assert_eq!(
            div(Expr::Value(i64::MIN), Expr::Value(-1)).eval(),
            Ok(1_i128 << 63)
        );
        assert_eq!(
            add(Expr::Value(i64::MAX), Expr::Value(i64::MAX)).eval(),
            Ok(2 * i128::from(i64::MAX))
        );
    }

    fn dimensions(expression: &Expr) -> (usize, usize) {
        match expression {
            Expr::Value(_) => (0, 1),
            Expr::Add(left, right) | Expr::Div(left, right) => {
                let (left_depth, left_leaves) = dimensions(left);
                let (right_depth, right_leaves) = dimensions(right);
                (1 + left_depth.max(right_depth), left_leaves + right_leaves)
            }
        }
    }

    #[test]
    fn public_recursive_generator_stays_within_the_exact_evaluation_domain() {
        hegel::Hegel::new(|tc: TestCase| {
            let expression = tc.draw(expressions());
            let (depth, leaves) = dimensions(&expression);
            assert!(depth <= 5);
            assert!(leaves <= 32);
            // May return DivisionByZero, but cannot panic on integer overflow.
            let _ = expression.eval();
        })
        .settings(
            hegel::Settings::from_profile("base")
                .seed(Some(42))
                .database(None)
                .test_cases(100)
                .phases([hegel::Phase::Generate])
                .suppress_health_check(hegel::HealthCheck::all()),
        )
        .run();
    }
}

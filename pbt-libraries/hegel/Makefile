.PHONY: benchmark run reports comparison test

benchmark: run
	python3 support/make_reports.py --update-readme

run:
	cargo build --release --locked
	@set -e; for challenge in $$(target/release/hegel-runner --list); do \
		target/release/hegel-runner --challenge $$challenge --seed 1337 --iterations 100; \
	done

reports:
	python3 support/make_reports.py

comparison:
	python3 support/make_reports.py --update-readme

test:
	cargo test --locked
	python3 -m unittest discover -s support -p 'test_*.py'

.PHONY: benchmark run reports comparison test

benchmark: run
	python3 support/make_reports.py --update-readme

run:
	cargo run --release --locked -- --iterations 100

reports:
	python3 support/make_reports.py

comparison:
	python3 support/make_reports.py --update-readme

test:
	cargo test --locked
	python3 -m unittest discover -s support -p 'test_*.py'

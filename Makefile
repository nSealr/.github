.PHONY: setup test lint audit docs ci

setup:
	@python3 -c "import yaml" 2>/dev/null || python3 -m pip install --user pyyaml

test:
	python3 scripts/verify_repo.py

lint:
	python3 scripts/verify_repo.py

audit:
	python3 scripts/verify_repo.py

docs:
	python3 scripts/verify_repo.py

ci: setup test lint audit docs


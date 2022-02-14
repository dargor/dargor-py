#
# Copyright (c) 2022, Gabriel Linder <linder.gabriel@gmail.com>
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
# AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
# INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
# LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
# OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
# PERFORMANCE OF THIS SOFTWARE.
#

all: help

help: ## show targets
	@cat $(MAKEFILE_LIST) \
		| grep -i "^[ a-z0-9_-]*: .*## .*" \
		| awk 'BEGIN {FS = ":.*?## "} \
		  {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

f flake8: ## run flake8
	flake8 .

b bandit: ## run bandit
	bandit -q -r -s B101 .

r radon: ## run radon
	radon cc .
	radon mi .

m mypy: ## run mypy
	mypy .

l lint: flake8 bandit radon mypy ## run linters

t test: ## run pytest
	pytest --cov

qa: lint test ## run linters and tests

sdist: clean ## build source distribution
	./setup.py sdist

wheel: clean ## build wheel [91m(old way, needs dev-python/wheel)[0m
	./setup.py bdist_wheel

build: clean ## build wheel [92m(new way, needs dev-python/build)[0m
	python -m build --wheel

pypi: build ## build wheel and upload to pypi
	twine upload dist/*

c clean: ## clean stuff
	rm -rf build dist *.egg-info
	find -L . -not -path './.git/*' -a \(  \
	          -iname __pycache__   -print0 \
	       -o -iname '*.py[co]'    -print0 \
	       -o -iname .mypy_cache   -print0 \
	       -o -iname .pytest_cache -print0 \
	       -o -iname .hypothesis   -print0 \
	       -o -iname .coverage     -print0 \
	       -o -iname .tox          -print0 \
	       -o -iname report.html   -print0 \
	       -o -iname tags          -print0 \
	\) | xargs -r0 rm -rf

#!/bin/sh
./scripts/load_all_fixtures.sh
pip install tox==3.20.0
tox -e${PYTHON_VERSION}
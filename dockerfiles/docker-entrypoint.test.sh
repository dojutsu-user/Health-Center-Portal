#!/bin/sh
pip install tox==3.20.0
tox -e${PYTHON_VERSION}
bash <(curl -s https://codecov.io/bash)

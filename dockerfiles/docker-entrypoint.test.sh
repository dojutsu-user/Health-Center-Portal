#!/bin/sh
pip install tox==3.20.0
pip install codecov
tox -e${PYTHON_VERSION}
curl -s https://codecov.io/bash > codecov.sh
chmod +x codecov.sh
./codecov.sh

#!/bin/bash

echo "Test Stage"

# install and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# install pip dependencies
pip3 install -r requirements.txt

#run pytest
python3 -m pytest \
  --cov=application \
  --cov-report term-missing \
  --junitxml=test-reports/unit-tests.xml \
  --cov-report xml:test-reports/coverage.xml

# deactivate and remove venv
deactivate
rm -rf venv

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
    --cov-report xml:coverage.xml \
    --junitxml=junit_report.xml

# deactivate and remove venv
deactivate
rm -rf venv

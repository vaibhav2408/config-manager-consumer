#!/bin/bash -ex

APP_DIR=${1:-app}
TESTS_DIR=${2:-"tests/unit_test"}

# shellcheck disable=SC2154
echo "Running unit tests with directory scope: $(pwd)"


# add the app source code to python path to accommodate
# imports as in the app source code
export PYTHONPATH=$PYTHONPATH:$(pwd)/${APP_DIR}

#echo "Setting aws credentials as host environment variables"
#export AWS_ACCESS_KEY_ID=test
#export AWS_SECRET_ACCESS_KEY=test
#export AWS_DEFAULT_REGION=us-west-2


# Run UTs
pytest \
    -p no:randomly \
    -vv \
    --exitfirst \
    --showlocals \
    --log-level ${LOGLEVEL:-"INFO"} \
    --log-cli-level ${LOGLEVEL:-"INFO"} \
    ${TESTS_DIR}

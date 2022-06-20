#!/bin/bash -ex

poetry config http-basic.jfrog $JFROG_USERNAME $JFROG_PASSWORD

poetry install --no-dev

poetry build

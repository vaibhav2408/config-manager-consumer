#!/bin/bash

# Update the correct URL for JFROG as per Adobe's configuration
poetry config repositories.publish-jfrog http://localhost:8081/artifactory/api/pypi/pypi-local

poetry publish -r publish-jfrog --username $JFROG_USERNAME --password $JFROG_PASSWORD

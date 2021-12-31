#!/bin/bash

echo "Deploy Stage"

scp docker-compose.yaml jenkins@ProductionServer:/home/jenkins/docker-compose.yaml 
ssh jenkins@ProductionServer \
    DOCKER_HUB_CREDS_USR=$DOCKER_HUB_CREDS_USR \
    docker stack deploy --compose-file docker-compose.yaml fantasybasketball_app 

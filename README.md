# Playing around with docker, mongodb and bottle

## Requirements

This script runs in docker so you need to have docker installed

# Simple app

Playing around with docker, mongodb small webservice

Uploads data and does a simple search query.


## Requirements

https://docs.docker.com/engine/installation/

Check installation with 
    
    docker --version

Make sure your user is added to the docker group on linux, otherwise you need root access.

## Build

Build the docker machine

    ./build_docker.sh

Run the docker container

    ./run_docker.sh

Once inside docker run 

    ./starup.sh 

Go to the link displayed in the container to run.






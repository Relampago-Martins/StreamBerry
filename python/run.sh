#!/bin/bash

docker run -it --rm --name streamberry -v ./app:/var/app -p 8000:8001 streamberry

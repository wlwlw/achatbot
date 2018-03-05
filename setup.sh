#!/bin/bash
docker rm achatbot
docker rmi achatbot
docker build -t achatbot
#export image if required
#docker save -o build/achatbot achatbot
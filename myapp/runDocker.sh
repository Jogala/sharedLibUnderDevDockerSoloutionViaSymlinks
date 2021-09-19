#!/bin/bash

docker kill $(docker ps -q)
docker build .  --no-cache -t node-web-app -f ./Dockerfile
docker run -p 49160:8080 -d node-web-app

containerid="$(docker ps | grep node-web-app| awk '{print $1}')"
echo "The container id is: $containerid"
#docker logs --follow $containerid
#docker exec -it "$(docker ps | grep node-web-app| awk '{print $1}')" ls -la node_modules
#docker exec -it "$(docker ps | grep node-web-app| awk '{print $1}')" /bin/bash

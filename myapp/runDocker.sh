#!/bin/bash


cd ../deployment
python3 replace_symlink_with_copy_of_module.py
cd ../myapp

docker kill $(docker ps -q)
docker build . -t jr/node-web-app

cd ../deployment
python3 replace_modules_with_symlinks.py
cd ../myapp


docker run -p 49160:8080 -d jr/node-web-app


containerid="$(docker ps | grep jr/node-web-app | awk '{print $1}')"
echo "The container id is: $containerid"
docker logs --follow $containerid
# docker exec -it "$(docker ps | grep node-web-app| awk '{print $1}')" ls -la node_modules
# docker exec -it "$(docker ps | grep node-web-app| awk '{print $1}')" /bin/bash

#!/bin/bash

printf "\nModifying Dockerfile and packages.json for docker build\n"
printf "####################################################################\n"
cd ../deployment
python3 replace_symlink_with_copy_of_module.py
python3 remove_local_packages_from_package_json.py
cd ../myapp

printf "\nBuild docker image\n"
printf "####################################################################\n"
docker kill $(docker ps -q)
docker build . -t jr/node-web-app

printf "\nUndo modifications\n"
printf "####################################################################\n"
cd ../deployment
python3 replace_modules_with_symlinks.py
python3 packages_tmp_to_packages.py
cd ../myapp

printf "\nRun docker image\n"
printf "####################################################################\n"
docker run -p 49160:8080 -d jr/node-web-app


containerid="$(docker ps | grep jr/node-web-app | awk '{print $1}')"
echo "The container id is: $containerid"
#docker logs --follow $containerid
# docker exec -it "$(docker ps | grep node-web-app| awk '{print $1}')" ls -la node_modules
# docker exec -it "$(docker ps | grep node-web-app| awk '{print $1}')" /bin/bash

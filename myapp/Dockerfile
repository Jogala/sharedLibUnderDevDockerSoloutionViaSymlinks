FROM node:latest
WORKDIR /usr/src/app
COPY . .
RUN npm install
EXPOSE 8080
EXPOSE 9229
RUN npm install -g nodemon
CMD [ "nodemon", "server.js" ]

FROM node:carbon-slim

# Create app directory
WORKDIR /transport_api

# Install app dependencies
COPY package.json /transport_api/
RUN npm install

# Bundle app source
COPY . /transport_api/
RUN npm run prepublish

CMD [ "npm", "run", "runServer" ]

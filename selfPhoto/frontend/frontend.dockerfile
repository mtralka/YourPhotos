FROM node:16 

# RUN npm install -g yarn --force
RUN yarn global add @quasar/cli

RUN mkdir /app



WORKDIR /app

# COPY /app /app

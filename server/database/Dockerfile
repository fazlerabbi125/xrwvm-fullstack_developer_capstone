FROM node:18.12.1-bullseye-slim

RUN npm install -g npm@9.1.3

COPY package*.json .
RUN npm install

ADD app.js .
ADD review.js .
ADD dealership.js .
ADD data/dealerships.json .
ADD data/reviews.json .
COPY . .

EXPOSE 3030

CMD [ "node", "app.js" ]

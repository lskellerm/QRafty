FROM node:21

WORKDIR /frontend

COPY package*.json ./
COPY yarn.lock ./                                               

RUN yarn install

COPY . .

EXPOSE 3000

# CMD ["yarn", "run", "dev"]
ENTRYPOINT [ "tail", "-f", "/dev/null"]    
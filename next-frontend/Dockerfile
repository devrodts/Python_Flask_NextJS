FROM node:20-alpine AS builder

WORKDIR /app

COPY package.json yarn.lock ./

RUN yarn install --frozen-lockfile

COPY . .

RUN yarn build

FROM node:20-alpine

WORKDIR /app

COPY --from=builder /app ./

COPY .env .env

EXPOSE 3000

ENV NODE_ENV=production

CMD ["yarn", "start"]

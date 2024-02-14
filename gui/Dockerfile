FROM node:20.11.0-alpine3.18

# RUN mkdir /app
WORKDIR /app
RUN chown node: /app

USER node

COPY --chown=node:node package.json .

RUN npm install && npm cache clean --force

COPY --chown=node:node . .

RUN npm run build

EXPOSE 3000

ENTRYPOINT ["/app/entrypoint.sh"]
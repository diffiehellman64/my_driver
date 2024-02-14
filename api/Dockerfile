FROM python:3.12.2-alpine3.19 as base

FROM base as builder
WORKDIR /install
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
COPY requirements.txt /
RUN pip install --prefix /install -r /requirements.txt

FROM base
RUN apk --no-cache add libpq ffmpeg
RUN addgroup -g 1000 django && adduser -u 1000 -G django -s /bin/sh -D django
WORKDIR /app
COPY --from=builder /install /usr/local
COPY --chown=django:django . .
EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]

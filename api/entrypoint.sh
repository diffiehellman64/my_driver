#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      echo "Waiting for postgres. While sleeping... Zzz"
      sleep 0.1
    done
    echo "PostgreSQL started!"
fi

exec "$@"
#!/bin/sh

DIR="/app/node_modules"
if [ ! -d "$DIR" ]; then
    echo "Installing modules..."
    npm install
    echo "Modules installed"
fi

exec "$@"
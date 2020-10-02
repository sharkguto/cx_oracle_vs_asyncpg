#!/bin/bash

echo "running"

echo "$0"

SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
    DIR="$(cd -P "$(dirname "$SOURCE")" >/dev/null 2>&1 && pwd)"
    SOURCE="$(readlink "$SOURCE")"
    [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR="$(cd -P "$(dirname "$SOURCE")" >/dev/null 2>&1 && pwd)"

echo "run at $DIR"

ls -la

# set -e

# echo "Running tests and check coverage"

# pytest --cov=benchx tests/ --cov-fail-under=70 --disable-pytest-warnings

echo "Start api"

#export LD_LIBRARY_PATH=/opt/oracle/instantclient_19_8/


gunicorn benchx:app --workers=4 -b "0.0.0.0:8080" --worker-class=uvicorn.workers.UvicornWorker --log-level info --timeout 60

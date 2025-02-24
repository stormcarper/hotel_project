#!/bin/bash

set -e

LOGLEVEL=${CELERY_LOGLEVEL:-INFO}
CONCURRENCY=${CELERY_WORKER_CONCURRENCY:-1}

QUEUE=${CELERY_WORKER_QUEUE:=celery}
WORKER_NAME=${CELERY_WORKER_NAME:="${QUEUE}"@%n}

echo "Starting celery worker $WORKER_NAME with queue $QUEUE"
exec celery worker \
    --app hotel_project \
    -Q $QUEUE \
    -n $WORKER_NAME \
    -l $LOGLEVEL \
    --workdir src \
    -O fair \
    -c $CONCURRENCY


#!/bin/bash
exec celery flower --app hotel_project --workdir src

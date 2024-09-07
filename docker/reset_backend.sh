#!/bin/bash

docker compose down
docker container rm postgres_db
docker volume rm docker_postgres_data 
docker compose up -d
sleep 3
docker compose run web python manage.py migrate
docker compose down
docker compose up
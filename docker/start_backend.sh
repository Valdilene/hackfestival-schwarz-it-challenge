#!/bin/bash

docker compose down
docker container rm postgres_db
docker volume rm docker_postgres_data 
docker compose up -d
sleep 3
docker compose run web python manage.py migrate

docker compose down
docker compose up -d

sleep 2
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"code": 1}' \
  http://127.0.0.1:8000/backend/api/store/

docker compose attach web
docker compose exec mongo mongodump &&
  docker compose cp mongo:/dump .

# DATABASE_URI = 'postgresql+psycopg2://postgres:1234@localhost/postgres'
from sqlalchemy import QueuePool

ENGINE_FUTURE = True
ENGINE_ECHO = True
ENGINE_POOL_SIZE = 10
ENGINE_MAX_OVERFLOW = 0


USER = "postgres"
PASSWORD = "1234"
# IP = "k8s-demo-fastapi-db" # test with docker compose
IP = "localhost" # local development

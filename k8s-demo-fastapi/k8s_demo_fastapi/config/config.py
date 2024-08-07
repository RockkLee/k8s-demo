# DATABASE_URI = 'postgresql+psycopg2://postgres:1234@localhost/postgres'
import os

from k8s_demo_fastapi.helper.log import logger

# Read environment variables first for production
ENGINE_FUTURE = os.getenv("PY_ENGINE_FUTURE", True)
ENGINE_ECHO = os.getenv("PY_ENGINE_ECHO", True)
ENGINE_POOL_SIZE = int(os.getenv("PY_ENGINE_POOL_SIZE", "10"))
ENGINE_MAX_OVERFLOW = int(os.getenv("PY_ENGINE_MAX_OVERFLOW", "0"))


USER = os.getenv("PY_DB_USER", "postgres")
PASSWORD = os.getenv("PY_DB_PASSWORD", "1234")
# IP = "k8s-demo-fastapi-db" # test with docker compose
# IP = "localhost" # local development
IP = os.getenv("PY_DB_IP", "localhost")

logger.info(f"{USER}:{PASSWORD}:{IP}")

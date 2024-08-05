import os

# Use uvicorn as the worker for the fastapi app
worker_class = 'uvicorn.workers.UvicornWorker'

# Number of worker processes (Recommendation: 2 * num_cpu +1)
workers = int(os.environ.get('GUNICORN_PROCESSES', '2'))

# timeout = int(os.environ.get('GUNICORN_TIMEOUT', '120'))
bind = os.environ.get('GUNICORN_BIND', '0.0.0.0:8080')
forwarded_allow_ips = '*'
# secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }


# run this command to start gunicorn server with your flask app
# gunicorn -c gunicorn_config.py <module-name>:<fastapi-instance-name>
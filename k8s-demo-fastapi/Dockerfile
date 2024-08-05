FROM python:3.11.0

# RUN apt-get update && apt-get install -y tree

# cd to the dir, and if the dir does not exist, create it
WORKDIR /fastapi-demo/

# Copy the necessary files and directories
COPY main.py ./
COPY k8s_demo_fastapi ./k8s_demo_fastapi
# COPY tests ./tests

# Copy the requirements.txt file
COPY requirements.txt ./
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8080

CMD ["gunicorn", "-c", "./k8s_demo_fastapi/config/gunicorn_config.py", "main:app"]
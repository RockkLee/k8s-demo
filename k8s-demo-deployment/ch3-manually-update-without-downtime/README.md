# Manually update without downtime
## Step 1: Build the 1.0.0 and 1.0.1 versions of the docker images locally for demo
- Edit the root API in the fastapi project for testing
    - Edit the file `k8s-demo-fastapi/main.py`

- For the version 1.0.0
```python
@app.get("/")
def root():
    return {"message": "Hello World v1.0.0"}
```

- For the version 1.0.1
```python
@app.get("/")
def root():
    return {"message": "Hello World v1.0.1"}
```

- Build the two versions of the docker images
    - `docker build -t k8s-demo-fastapi:1.0.0 .`
    - `docker build -t k8s-demo-fastapi:1.0.1 .`

<br>

## Step 2: Set up the environment
- Run `old-pod.yml` to create the pod with the version 1.0.0.
    - ` kubectl apply -f old-pod.yml`

- Run `services.yml` to create the service for the pod.
    - ` kubectl apply -f services.yml`

- Run curl continuously to check if the app is alive
    - `watch -n 2.0 curl http://localhost:30000/`

<br>

## Step 3: Conduct the update process manully
(Services recognize pods based on labes.app and labels.release with selector.app and selector.release)

- Run `new-pod.yml` to create the new version of the pod with version 1.0.1
    - ` kubectl apply -f new-pod.yml`

- Revise `service.yml` to set the selector.release to 1.0.1 and run it

- Delete the old pod.
    - ` kubectl delete k8s-demo-fastapi-1.0.0`
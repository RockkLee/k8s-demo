# K8S Deployments
## Note
- A Deployment is an object that runs a pod spec with multiple instances.
- It can also update pods without downtime.
- A deployment is an object that helps pods be updated without downtime.
- It controls another object called a replicaset, and the replicaset can run a pod spec with multiple instances.

## Steps to demonstrate updating apps without downtime by using deployments
(The old replicaset won't be deleted after the update because the deployment stores the last 10 rollouts to allow rollback to previous versions)

- Run curl continuously to check if the app is alive.
    - `watch -n 1.0 curl http://localhost:30000/`

- Run `k8s-demo-fastapi.yml`
    ` kubectl apply -f k8s-demo-fastapi.yml`

- Change `template.spec.image` from version 1.0.0 to 1.0.1

- Uncomment `spec.minReadySeconds` for demonstration

- Run `k8s-demo-fastapi.yml` again
    - ` kubectl apply -f k8s-demo-fastapi.yml`
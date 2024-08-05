# Database and Persistent data in K8S
## Static Persistent Volume vs. Dynamic Persistent Volume
### Static Persistent Volume (This is used in this chapter)
```
    *************           *************
    *    Pod    *           *    Pod    *
    *************           *************
          |                       |
    *************           *************
    *    PVC    *     ,     *    PVC    *     ,  ......
    *************           *************
          |                       |
    *************           *************
    *    PV     *           *    PV     *
    *************           *************
```

### Dynamic Persistent Volume
```
    *************           *************
    *    Pod    *           *    Pod    *
    *************           *************
          |                       |
    *************           *************
    *    PVC    *           *    PVC    * 
    *************           *************
          |                       |
    *************************************
    *            StorageClass           *
    *************************************
          |                       |
        (Generate PV by StorageClass)
          |                       |
    *************           *************
    *    PV     *           *    PV     *
    *************           *************
```

### Steps to demonstrate how to create a database in k8s
- Create a ConfigMap to set the database's account and password
    - `kubectl apply -f configmap.yml`
    - `kubectl get configmaps`
    - `kubectl describe configmap <name>`
- Create a PV and a PVC for mounting a volume to prevent data loss after shut down
    - `kubectl apply -f storage.yml`
    - `kubectl get pvc`
    - `kubectl describe pvc <name>`
    - `kubectl get pv <name>`
    - `kubectl describe pv <name>`

- Create a deployment to run the database
    - `kubectl apply -f postgresql.yml`

- Run port-forwarding to allow  postgresql client app to connect to the database for testing
    - `kubectl port-forward svc/postgresdb 5432:5432`
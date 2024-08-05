# Create a service
## Note
- A service is an object that controls the network of pods.
- Services and pods don't have to be written in different yml files.
- I write the yml files based on the features, so Pods, Services, Developments, etc., might be written in the same yml files.

<br>

## The types of services
### ClusterIP
This is the **default** type for service in Kubernetes.
As indicated by its name, this is just an address that can be used inside the cluster.

<br>

### NodePort
A NodePort **exposes a port in each Node**.

### LoadBalancer
(It can only be used on the cloud platform, such as GKE, EKS, etc.)
A LoadBalancer is a Kubernetes service that:
- Creates a service like ClusterIP
- Opens a port in every node like NodePort
- Uses a LoadBalancer implementation from your cloud provider

<br>

## Steps to create a service and a pod.
- Write a yml file to run a pod and a service
    - `k8s-demo-fastapi.yml`

- Run a pod and a service by running the yml file.
    - `kubectl apply -f k8s-demo-fastapi.yml`

- Check the APIs in the web service.
    - `http://localhost:30000/docs`
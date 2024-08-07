# Create a pod
## Useful commands to create a pod
- Create pods, services, etc., by running the yml file.
```bash
kubectl apply -f <the yml filename> # create pods,services, etc by a yml file
```

- Read the information about a pod.
```bash
# List all objects that you’ve created. Pods at first, later, ReplicaSets, Deployments and Services.
kubectl get all

# List all pods along with containers' status.
kubectl get pods

# List all pods from different namespaces along with containers' status.
kubectl get pods -A

# Obtain deeper information about a pod.
kubectl describe pod <pod-name>
```

- Delete a pod
```bash
kubectl delete pod <pod-name>
```

- Interact with a pod
```bash
# execute a command in the pod
kubectl exec  <pod-name> -- <command>

# enter the pod with the terminal
kubectl exec -it <pod-name> -- sh
```

- Test DNS
```bash
kubectl run -i --tty --rm dns-test --image=busybox --restart=Never -- nslookup <domain-name>
```

## Steps for creating a pod and check if it works or not
- Write a yml file to run a pod
    - `pods.yml`

- Run a pod with the yml file
    - `kubectl apply -f <the yml filename>`

- Check if the pod runs correctly
    - `kubectl get pods`

- Since we can't connect to the web service inside the pod currently, 
- We can only enter the pod with terminal to check if the web app is running.
    - kubectl exec -it <pod-name> -- sh
    - curl -X GET "http://localhost:<port-number>/<url>"
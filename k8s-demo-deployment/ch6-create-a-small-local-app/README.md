# Create a small local app
## Steps to demonstrate how to deploy a small app in K8S
- Set up the domain name for Ingress.
    - Edit `C:\Windows\System32\drivers\etc` and add the below code.
```
# k8s demo
127.0.0.1 k8s-demo
127.0.0.1 k8s-demo-fastapi-app
```
- Run all YML files in ch6 directores

<br>

## Ingress
- Use Ingress to transfer requests from clients, eg. browser, to pods.
- Using NodePort is not recommended.
    - The reason is we cannot just expose the frontend port because the APIs, which are used by frontend, also need to be exposed.
    - This is because the browser doesn't know the domain names inside the k8s, whereas the pods running the frontend apps are the ones that actually know them.

<br>

## Frontend
### Use ConfigMap as Kubernetes Volumes
- Because the frontend (React) cannot read the env variables since most frontend frameworks are browser-side frameworks, we cannot use ConfigMap directly.
- Therefore, we need to combine ConfigMap, development.Volumes, and development.volumeMounts to set up env variables.
- The implementation is that we create a file, called `configmap.js`, in the react public directory and expose it in `public/index.html`.
- Then, we mount `configmap.js` by ConfigMap, development.Volumes, and development.volumeMounts in `/usr/share/nginx/html/configmap.js`.
- Finaly, the env variables are read by React in `util/Api.js`.

<br>

## Backend
### Use Regular ConfigMap
Set up the ConfigMap in the common way and read the env variables by `os.getenv` in Python.

## Database for Backend
The configurations are basically the same as ch5.
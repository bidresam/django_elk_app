# django_elk_app
A python app bulit using django web framework using elasticsearch as a DB that maintains a list of cities and their population and exposes 3 endpoints:healthcheck,adding a city with its population and listing cities

Please follow below steps for app installation

---


## Create Docker images
Create app docker image
```
cd <Path to project>/django-elk/django_elk
docker build -t overwatch563/django-app-demo:v1 --file ./Dockerfile.prod .  
docker push overwatch563/django-app-demo:v1
```

Create Nginx docker image
```
cd <Path to project>/django-elk/nginx
docker build -t overwatch563/django-app-demo:nginx-v1 -f ./Dockerfile.prod .
docker push overwatch563/django-app-demo:nginx-v1
```

Deploy application in Kubernetes
```
cd <Path to project>/django-elk/k8s
# Deploy elasticsearch pods
kubectl apply -f elastic-deployment.yml
# Check for pods to start 
kubectl get po
# Deploy service 
kubectl apply -f elastic-service.yml
# Deploy web app pods
kubectl apply -f webapp-deployment.yml
# Check for pods to start 
kubectl get po
# Deploy service 
kubectl apply -f app-service.yml
# Port forward to access the application web ui
kubectl port-forward service/app-service 7080:80
```

To try the local setup using docker-compose
```
cd <Path to project>
docker-compose -f docker-compose.qa.yml up --build -d

```

Other useful docker commands for reference
```
docker-compose -f docker-compose.qa.yml ps -a
Formatting of `docker ps` output to strip ports - useful to set as an alias if mapping many ports produces large, wrapped output :
docker ps --format "table{{.ID}}\t{{.Names}}\t{{.Image}}\t{{.RunningFor}}\t{{.Status}}"
To execute command on a running container OR take a docker into interactive mode :
docker exec -it es-container bash
To remove unused docker images:
docker image prune -a
```
Reference:
```
overwatch563 is my dockerhub username(Sampath's)
<Path to project> is the absolute filepath where this repo is cloned on your local machine
The app has been tested and deployed successfully on a macbook using docker desktop version 2.3.0.4 on a minikube whose resources are cpu:4cores,memory:8GB,swap:1GB,diskspace:59.6GB
TobeWorked: Helmdeployment.
Current app deployment is via K8s.Good article for my future reference : https://phoenixnap.com/kb/create-helm-chart
```
Sample Screenshots of the k8s application :

Main Landing page:
[![Screenshot-2022-10-05-at-6-12-21-PM.png](https://i.postimg.cc/BnLHv57b/Screenshot-2022-10-05-at-6-12-21-PM.png)](https://postimg.cc/hXnfymBR)

Health Endpoint URL:
[![Screenshot-2022-10-05-at-6-16-36-PM.png](https://i.postimg.cc/LXMbD8gk/Screenshot-2022-10-05-at-6-16-36-PM.png)](https://postimg.cc/B8MpQsgt)

Add City Endpoint URL:
[![Screenshot-2022-10-05-at-6-14-11-PM.png](https://i.postimg.cc/t4jnX06S/Screenshot-2022-10-05-at-6-14-11-PM.png)](https://postimg.cc/Wh51nHXg)

List Cities Endpoint URL:
[![Screenshot-2022-10-05-at-6-18-36-PM.png](https://i.postimg.cc/pXDYQJYS/Screenshot-2022-10-05-at-6-18-36-PM.png)](https://postimg.cc/VdkCmMh9)

---

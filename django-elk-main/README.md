**Django ELK Sample App**
Please follow below steps for app installation

---


## Create Docker images
Create app docker image
```
cd <Path to project>\django-elk\django_elk
docker build -t overwatch563/django-app-demo:v1 --file .\Dockerfile.prod .  
docker push overwatch563/django-app-demo:v1
```

Create Nginx docker image
```
cd <Path to project>\django-elk\nginx
docker build -t overwatch563/django-app-demo:nginx-v1 -f ./Dockerfile.prod .
docker push overwatch563/django-app-demo:nginx-v1
```

Deploy application in Kubernetes
```
cd <Path to project>\django-elk\k8s
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
---
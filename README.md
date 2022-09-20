# Assessment

## 1. Create a simple http server and build an image out of it 

 Created Python server that handles GET and POST requests 
 Created an image via the Dockerfile (consider it named : simple-server:v1)
 
## 2. Create deployments to deploy this app with 3 replication and create a service type of load balancer to load balance and access this application

 Created deployment with 3 replicas yaml
 Created a service of type LoadBalancer pointing to the port 8080 of the server
 
# micro-app-4-bbk
Microservice app_4 of web app for MSc Data Science project repo (microservice auto-scaling system)

# Description

Application summary as part of test microservice based web application (seen in 2019 N C Coulson paper: "Adaptive microservice scaling for elastic web applications")

App 4 makes a request to an open API (http://numbersapi.com) using the input number as a parameter. Then returns the length of the response text multiplied by 12. App 4 is particularly interesting because it exposes the system to further unknown variables, like external network latency, which may in turn add more variability to the response time data. 

# Deployment
This github repo is linked to a DockerHub repo (https://cloud.docker.com/u/certainnathan/repository/docker/certainnathan/micro-app-4-bbk) which is referenced in the Swarm deployment YAML config file. Any accepted changes will be automatically incorporated into the latest Docker image used in the main application.

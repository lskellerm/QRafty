# !/bin/bash

# Navigate to the root directory of the backend project 
cd ../../backend/

# Build the docker image
docker build -t qrafty-backend:latest .


# Stop and remove the existing container
docker stop qrafty-backend-1
docker rm qrafty-backend-1

# Clean up and remove dangling image from the previous build
docker image prune -f 

# Create and run a new container from the updated image
docker run -d --name qrafty-backend qrafty-backend:latest 
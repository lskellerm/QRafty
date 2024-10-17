# !/bin/bash

# Navigate to the root directory of the backend project 
cd ../../backend/

# Build the docker image
docker build --target dev -t qrafty-backend:latest .


# Stop and remove the existing container if it exists
docker stop qrafty-backend-1 2>/dev/null || true
docker rm qrafty-backend-1 2>/dev/null || true

# Clean up and remove dangling image from the previous build
docker image prune -f 

# Create and run a new container from the updated image
docker run -d --name qrafty-backend qrafty-backend:latest 
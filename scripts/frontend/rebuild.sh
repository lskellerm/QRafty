# !/bin/bash

# Navigate to the root directory of the frontend project 
cd ../../frontend/

# Build the docker image
docker build --target dev -t qrafty-frontend:latest .


# Stop and remove the existing container if it exists
docker stop qrafty-frontend-1 2>/dev/null || true
docker rm qrafty-frontend-1 2>/dev/null || true

# Clean up and remove dangling image from the previous build
docker image prune -f 

# Create and run a new container from the updated image
docker run -d --name qrafty-frontend qrafty-frontend:latest 
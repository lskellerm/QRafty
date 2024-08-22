# !/bin/bash

# Convenience utility script to clean up docker images and volumes, removing any dangling versions no longer in use

# Remove all dangling images
docker rmi $(docker images -f "dangling=true" -q)

# Remove all dangling volumes
docker volume rm $(docker volume ls -qf dangling=true)


# !/bin/bash

# This script is used to setup the ephemeral test database for clean test runs.
# Leverages alembic migration scripts to perform the setup.

# Open a shell in the backend container (used for the python environment and alembic)
docker exec -it qrafty-backend-1 /bin/bash -c "
    cd backend && \
    export ENVIRONMENT=testing && \
    alembic upgrade head "

echo "Database setup completed successfully and ready for testing"


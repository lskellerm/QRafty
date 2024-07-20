FROM python:3.12

WORKDIR /workspace

RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip to the latest version
RUN python -m pip install --upgrade pip

# Copy the Python requirements file
COPY requirements.txt ./
COPY dev-requirements.txt ./

# Install the Python Dependencies
RUN pip install --no-cache-dir -r dev-requirements.txt

COPY . .

EXPOSE 8000

# Keeps the container running, used for initially setting up dev environment in container
ENTRYPOINT ["tail", "-f", "/dev/null"]    

# Remove when ready to continously run the FastAPI app
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]





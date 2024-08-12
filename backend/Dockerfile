# Stage 1: Base Image
FROM python:3.12-slim AS base           

WORKDIR /workspace

# Install build-essential for compiling necessary packages and install the Python Dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/* \ 
    && pip install --no-cache-dir --upgrade pip

# Stage 2: Development Image
FROM base as dev

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy and install the Python Dependencies specific for development
COPY dev-requirements.txt ./
RUN pip install --no-cache-dir -r dev-requirements.txt

# Copy applicaiton code
COPY . .

# Expose the port for FastAPI dev server
EXPOSE 8000

# Keeps the container running, used for keeping the container running for development
ENTRYPOINT ["tail", "-f", "/dev/null"]    

# Stage 3: Production Image
FROM base as prod

# Copy applicaiton code
COPY . .

# Copy and install the Python Dependencies specific for production
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt && \
    apt-get purge -y build-essential && \
    apt-get autoremove -y && \  
    rm -rf /root/.cache/pip /var/lib/apt/lists/* && \
    rm -rf .coverage htmlcov .coveragerc dev-requirements.in dev-requirements.txt .pytest_cache pytest.ini tests .ruff_cache .venv

# Expose the port for FastAPI app
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]





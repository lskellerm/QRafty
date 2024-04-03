FROM python:3.12

WORKDIR /workspace

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Keeps the container running, used for initially setting up dev environment in container
ENTRYPOINT ["tail", "-f", "/dev/null"]    

# Remove when ready to continously run the FastAPI app
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

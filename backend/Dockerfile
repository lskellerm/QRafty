FROM python:3.12

WORKDIR /workspace/

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Keeps the container running

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
ENTRYPOINT [ "tail", "-f", "/dev/null" ]
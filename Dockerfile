FROM python:3.11-slim

WORKDIR /app

COPY . /app

ENV BITBUCKET_TOKEN=valor1
ENV BITBUCKET_WORKSPACE=valor2
ENV BITBUCKET_USERNAME=valor2
ENV BITBUCKET_PASSWORD=valor2

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "main.py"]
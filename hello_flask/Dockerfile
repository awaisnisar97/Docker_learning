FROM python:3.8-slim as Build 

WORKDIR /app

# Install system dependencies FIRST (this is the fix)
RUN apt-get update && apt-get install -y \
    gcc \
    pkg-config \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir flask mysqlclient

#stage 2 production stage 

FROM python:3.8-slim

WORKDIR /APP 

COPY --from=Build /app /app 

EXPOSE 5002

CMD ["python", "app.py"] 


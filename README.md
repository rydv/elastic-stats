# FastAPI Application with Elasticsearch

This FastAPI application connects to an Elasticsearch instance to manage and query transaction data. The application includes endpoints for adding transactions and checking the health of the Elasticsearch connection.

## Project Structure
```
my_fastapi_app/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── elasticsearch_client.py
│   └── routers/
│       ├── __init__.py
│       ├── transactions.py
│       └── health_check.py
├── Dockerfile
├── requirements.txt
└── .env
```


## Prerequisites

- Python 3.9+
- Docker (for running Elasticsearch)

## Setup

### Step 1: Clone the Repository

```sh
git clone https://github.com/your-repo/elastic_stats.git
cd elastic_stats
```

### Step 2: Create python environment
```
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
pip install -r requirements.txt
```

### Step 3: Run elastic on docker
```
docker network create elastic
docker pull docker.elastic.co/elasticsearch/elasticsearch:8.14.1
docker run --name es01 --net elastic -p 9200:9200 -e "discovery.type=single-node" -e "xpack.security.enabled=false" docker.elastic.co/elasticsearch/elasticsearch:8.14.1
```

### Step 4: Set environment variables
```
PYTHONPATH=./app
ELASTICSEARCH_HOST=https://localhost:9200
ELASTICSEARCH_USER=your_username
ELASTICSEARCH_PASSWORD=your_password
```

### Step 5: Run the application
```
uvicorn app.main:app --reload
```



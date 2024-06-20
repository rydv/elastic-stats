# app/utils/elasticsearch_client.py

from elasticsearch import Elasticsearch
from app.config.config import settings

es = Elasticsearch(
    [settings.elasticsearch_host],
    http_auth=(settings.elasticsearch_user, settings.elasticsearch_password),
    # scheme="https",
    # port=9200,
    verify_certs=False  # This should be True in production with proper certificate handling
)

def get_elasticsearch_client():
    return es
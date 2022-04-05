import os
from enum import Enum
from pymongo import MongoClient

client = MongoClient(
    os.environ['MONGODB_HOSTNAME'], 27017,
    username=os.environ['MONGODB_USER'],
    password=os.environ['MONGODB_PASSWORD']
)

class UrlTypes(Enum):
    STANDARD = 'http://'

def route(url_hash):
    query_res = client['urlshortener_db']['url_mappings'].find_one({'url_hash': url_hash})
    if query_res is None:
        return None
    else:
        return query_res['original_url']

def format_url(url_string):
    if UrlTypes.STANDARD in url_string:
        return url_string
    else:
        return UrlTypes.STANDARD + url_string

import base62
import os
from pymongo import MongoClient
client = MongoClient(
    os.environ['MONGODB_HOSTNAME'], 27017,
    username=os.environ['MONGODB_USER'],
    password=os.environ['MONGODB_PASSWORD']
)


def shorten(url):
    url_hash = base62.encode(abs(hash(url)))
    client['urlshortener_db']['url_mappings'].insert_one({
        'url_hash': url_hash,
        'original_url': url,
    })
    return url_hash

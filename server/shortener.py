import base62

SHORTENED_URL_PREFIX = 'urlify.com/'
TEMP_DB = {}


def shorten(url):
    url_hash = base62.encode(abs(hash(url)))
    if url_hash not in TEMP_DB:
        TEMP_DB[url_hash] = url
    short_url = url_hash
    return short_url


def route_to_original(url_hash):
    if url_hash not in TEMP_DB:
        return None
    else:
        return TEMP_DB[url_hash]

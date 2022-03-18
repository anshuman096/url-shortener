import base62

SHORTENED_URL_PREFIX = 'urlify.com/'
TEMP_DB = {}


def shorten(url):
    print("original url: ", url)
    url_hash = base62.encode(abs(hash(url)))
    if url_hash not in TEMP_DB:
        print("IN HERE")
        TEMP_DB[url_hash] = url
    short_url = SHORTENED_URL_PREFIX + url_hash
    return short_url

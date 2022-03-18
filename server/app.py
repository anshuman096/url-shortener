from flask import abort, Flask, request, redirect

from shortener import route_to_original, shorten

app = Flask(__name__)


@app.route('/<url_hash>', methods=['GET'])
def routeToUrl(url_hash):
    original_url = route_to_original(url_hash)
    if original_url:
        return redirect("http://" + original_url, 301)
    else:
        return abort(404)


@app.route('/shorten', methods=['POST'])
def shortenUrl():
    payload = request.json
    shortened_url = shorten(payload['url'])
    return shortened_url


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

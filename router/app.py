from flask import abort, Flask, redirect

from router import route

app = Flask(__name__)


@app.route('/<url_hash>', methods=['GET'])
def routeUrl(url_hash):
    original_url = route(url_hash)
    if original_url:
        return redirect("http://" + original_url, 301)
    else:
        return abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

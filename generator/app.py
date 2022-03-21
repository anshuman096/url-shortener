from flask import Flask, request

from generator import shorten

app = Flask(__name__)


@app.route('/shorten', methods=['POST'])
def shortenUrl():
    payload = request.json
    shortened_url = shorten(payload['url'])
    return shortened_url


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

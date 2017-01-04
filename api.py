"""Service to return a sert of counters defined in REDIS."""
from __future__ import print_function
from flask import Flask, jsonify
from flask_redis import FlaskRedis
import os
import sys

app = Flask(__name__)

pwd = os.environ.get('REDIS_PASSWORD')
host = os.environ.get('REDIS_HOST')

if pwd:
    pwd = ":" + pwd
else:
    pwd = ""

REDIS_URL = "redis://" + pwd + "@" + host + ":6379"
app.config['REDIS_URL'] = REDIS_URL

redis_store = FlaskRedis(app)


@app.route('/<counters>', methods=['GET'])
def list_messages(counters):
    """List Counters."""
    keys = counters.split(",")
    resp = {}
    for key in keys:
        resp[key] = redis_store.get(key).decode('utf-8')

    print(resp, file=sys.stderr)
    return jsonify(counters=resp)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
        threaded=True)

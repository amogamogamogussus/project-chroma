from flask import *
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def root():
    payload = {
        "content-type": "application/json; charset=UTF-8",
        "content": {
            "data": "This is a default message!",
            "bytes": 25,
        },
        "connection": "Connected via a endpoint.",
        "Status Code": 200
    }
    resp = make_response(payload)
    resp.headers['server'] = 'testing'
    resp.headers['Date'] = datetime.now()
    resp.headers['Content-Type'] = 'application/json; charset=UTF-8'
    return resp

if __name__ == "__main__":
    app.run(host="localhost", port=8888, debug=True)
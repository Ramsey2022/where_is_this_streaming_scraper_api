from . import app
import json
from flask import jsonify, request, make_response, abort, url_for


# Return message
@app.route("/")
def root():
    return {"message": "Server is running!"}


# Return health of the app
@app.route("/health")
def health():
    return jsonify(dict(status="OK")), 200

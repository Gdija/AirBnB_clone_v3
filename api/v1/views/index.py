#!/usr/bin/python3
"""index blueprint """
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """get status information"""
    return jsonify({"status": "OK"})

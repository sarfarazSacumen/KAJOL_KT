"""Mocking for API
"""
from requests import Response
import json

def mock_api_success():
    """Mock for API success response"""
    data = {"key": "Success"}
    response = Response()
    response.status_code = 200
    response._content = bytes(json.dumps(data), encoding="utf-8")
    return response
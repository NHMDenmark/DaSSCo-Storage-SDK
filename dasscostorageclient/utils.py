import requests
from enum import Enum
from exceptions.api_error import APIError


class RequestMethod(Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'


def send_request(method: RequestMethod, token: str, path: str, json: dict = None):
    headers = {
        'Authorization': f"Bearer {token}",
        'Content-Type': 'application/json',
    }

    api_url = f"https://storage.test.dassco.dk/api{path}"

    res = requests.request(method.name, headers=headers, url=api_url, json=json)

    if res.status_code == 200:
        return {
            'data': res.json(),
            'status_code': res.status_code
        }
    else:
        raise APIError(response=res.json(), status_code=res.status_code)

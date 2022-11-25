from requests import Session
from consts import url, headers
from credentials import api_key
from params import params


def _connection(start: int, end: int):
    content = params(api_key)
    s = Session()
    response = s.post(url=url, json=content, headers=headers)
    return response.json()

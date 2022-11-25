from requests import Session
from consts import url, headers
from credentials import api_key
from params import params


def _connection():
    content = params(api_key)
    s = Session()
    response = s.post(url=url, json=content, headers=headers)
    return response.json()


print(_connection())


class Random:
    pass

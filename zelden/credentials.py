# TODO: Implement the credentials file

import os
from exceptions import CredentialsError


class APIKEY:
    apikey: str = os.getenv('APIKEY')
    if not apikey:
        apikey = ''
        if not apikey:
            raise CredentialsError('No credentials found')

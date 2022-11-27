import os
from exceptions import CredentialsError


class APIKEY:
    apikey: str = os.getenv('APIKEY')
    if not apikey:
        raise CredentialsError('No credentials found. Set it with set_credentials function')

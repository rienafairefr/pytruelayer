import json

from truelayer.auth.configuration import Configuration
from truelayer.auth.api_client import ApiClient
from truelayer.auth.api.default_api import DefaultApi

credentials = json.load(open('../.secrets/secrets.json'))

configuration = Configuration(host='https://auth.truelayer.com')
api_client = ApiClient(configuration)
api = DefaultApi(api_client)

code = input('code')

token = api.exchange_code(
    client_id=credentials['client_id'],
    client_secret=credentials['client_secret'],
    redirect_uri=credentials['redirect_uri'],
    code=code,
    grant_type='authorization_code'
)

pass

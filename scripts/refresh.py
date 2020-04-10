import json

from truelayer.api import DataApi
from truelayer.auth.api import AuthApi

credentials = json.load(open('../.secrets/secrets.json'))

user = credentials['test_user']

data_api = DataApi()
auth_api = AuthApi()
configuration = data_api.api_client.configuration

configuration.host = credentials['host']
configuration.access_token = user['access_token']

refreshed = auth_api.exchange_code(
    credentials['client_id'],
    credentials['client_secret'],
    credentials['redirect_uri'],
    'refresh_token',
    refresh_token=user['refresh_token']
)

print('refreshed %s' % refreshed.to_dict())
configuration.access_token = refreshed.access_token


data_api.api_client.configuration.host = credentials['host']
data_api.api_client.configuration.refresh_api_key_hook = refresh_api


print(data_api.me_get().to_dict())
print(data_api.accounts_get())

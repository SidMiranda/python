import hashlib
import hmac
import json

from http import client
from urllib.parse import urlencode

MB_TAPI_ID = ''
MB_TAPI_SECRET = ''
REQUEST_HOST = 'www.mercadobitcoin.net'
REQUEST_PATH = '/tapi/v3/'

params = {
    'tapi_method': 'place_market_buy_order', #'get_account_info',
    'tapi_nonce': 4,
    'coin_pair': 'BRLETH',
    'cost': '2.58',
    #'limit_price': '1195.90000'
}

params = urlencode(params)

params_string = REQUEST_PATH + '?' + params
H = hmac.new(MB_TAPI_SECRET.encode(), digestmod=hashlib.sha512)
H.update(params_string.encode())
tapi_mac = H.hexdigest()

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'TAPI-ID': MB_TAPI_ID,
    'TAPI-MAC': tapi_mac
}

try:
    conn = client.HTTPSConnection(REQUEST_HOST)
    conn.request("POST", REQUEST_PATH, params, headers)

    response = conn.getresponse()
    response = response.read()

    response_json = json.loads(response)
    print('status: {}'.format(response_json['status_code']))
    print(json.dumps(response_json, indent=4))
finally:
    if conn:
        conn.close()

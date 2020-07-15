from requests import get
import json
from time import sleep

coin = 'eth'

while True:
    dados = get('https://www.mercadobitcoin.net/api/'+coin+'/ticker')
    price = json.loads(dados.text[11:-1])['last']
    print(price)
    sleep(2)

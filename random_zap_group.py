import requests
import time
import selenium

x = requests.get('https://gruposwhats.app/join-group/')
n = 400

with open('lista.csv', 'w') as _file:
    while n < 500:
        time.sleep(0.5)
        x = requests.get('https://gruposwhats.app/join-group/' + str(n))
        if x.status_code == 200:
            _file.write(str(n))
            print(x.status_code, 'https://gruposwhats.app/join-group/'+ str(n))
        n = n + 1

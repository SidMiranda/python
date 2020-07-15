import time, datetime, timedelta
import gspread
import requests, sys, os
from oauth2client.service_account import ServiceAccountCredentials

def nome(ramal):
    if ramal == 2020:
        return 'Chrysthyanne'
    elif ramal == 2027:
        return 'Fabio'
    elif ramal == 2023:
        return 'Ivan'
    elif ramal == 2019:
        return 'Fernando'
    elif ramal == 2012:
        return 'Marcos'
    elif ramal == 2021:
        return 'Eduardo'
    elif ramal == 2014:
        return 'Plinio'
    elif ramal == 2024:
        return 'Caio'
    elif ramal == 2004:
        return 'Jefferson'

    return 'Nobody'


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('sidHost-clientSecret.json', scope)
client = gspread.authorize(creds)
sheet = client.open('Intelix').sheet1
#Intelix = sheet.get_all_records()

ramais = (2004, 2012, 2014, 2019, 2020, 2021, 2023, 2024, 2027)
URL = 'http://192.168.10.35/intelix/integracao/intAttendantIntelix.php'

index = 2
while True:
    try:
        for ramal in ramais:
            DATA = {"auth": "a49717818443b1acea0bd25111215f1e", "action": "status", "agent": ramal}
            response = requests.post(URL, DATA)
            print(response.content)
            sheet.update_cell(index, 1, str(response.content)[93:])
            tempo = sheet.cell(index, 5).value
            if str(response.content)[93:] == "true}'":
                sheet.update_cell(index, 5, str(int(tempo) + 1))
            index += 1
            time.sleep(5)

        time.sleep(15)
        index = 2
    except ValueError:
        print(ValueError)
        time.sleep(30)
        index = 2

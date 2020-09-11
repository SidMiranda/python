import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('netWorkManage.json', scope)
client = gspread.authorize(creds)
sheet = client.open('HostControl').sheet1

teste = sheet.cell(1, 2).value

sheet.update_acell('C1', 'HOST ALIVE CABROM')

print(teste)

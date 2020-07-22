import pyodbc
import datetime
import telepot
from time import sleep

#botX9
botAPI = 'XXX'
bot = telepot.Bot(botAPI)
msgCPD = -XXX

con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\admin.XXX\AppData\Local\VirtualStore\Program Files (x86)\Trix Tecnologia\Finger Config II\att2000.mdb')
sql = ('SELECT TOP 1 A.NAME, B.USERID, B.CHECKTIME, B.SENSORID ' +
        'FROM USERINFO AS A INNER JOIN CHECKINOUT AS B ON A.USERID = B.USERID ORDER BY B.CHECKTIME DESC')

lastCheck = ''
cursor = con.cursor()

while True:
    sleep(10)
    cursor.execute(sql)
    try:
        for row in cursor.fetchall():
            if row[3] == '2':# se o id do sensor for 2(CPD)
                if lastCheck != row[2]:
                    bot.sendMessage(msgCPD, 'Acesso ao CPD \n ' + row[0] + ' as ' + str(row[2])[11:16])
                    lastCheck = row[2]
    except:
        bot.sendMessage(msgCPD, 'APLICAÇÃO PAROU! \n ' + str(datetime.datetime.now()))
        sleep(60)
        pass

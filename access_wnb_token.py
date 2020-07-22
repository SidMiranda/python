import pyodbc, sys
import time, datetime
import telepot
import funcionarios

botAPI = 'XXX'
bot = telepot.Bot(botAPI)
msgSid = XXX
msgCPD = -XXX
msgNOC = -XXX
con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\admin.XXX\AppData\Local\VirtualStore\Program Files (x86)\Trix Tecnologia\Finger Config II\att2000.mdb')
sql = 'SELECT TOP 1 A.NAME, B.USERID, B.CHECKTIME, B.SENSORID FROM USERINFO AS A INNER JOIN CHECKINOUT AS B ON A.USERID = B.USERID ORDER BY B.CHECKTIME DESC'
lastCheck = ''

cursor = con.cursor()

while True:
    try:
        cursor.execute(sql)
        for row in cursor.fetchall():
            #print(row)
            if row[3] == '2':# se o id do sensor for 2(CPD)
                if lastCheck != row[2]:
                    bot.sendMessage(msgCPD, 'Acesso ao CPD \n ' + row[0] + ' as ' + str(row[2])[11:16])
                    #print(row[0])
                    lastCheck = row[2]
                    pass
            elif funcionarios.isnoc(row[1]) == 'yes':# se o funcionario for do NOC
                if lastCheck != row[2]:
                    bot.sendMessage(msgNOC, 'Entrada/Saida \n ' + row[0] + ' as ' + str(row[2])[11:16])
                    #print(row[0])
                    lastCheck = row[2]
                    pass
        time.sleep(10)
    except:
        bot.sendMessage(msgCPD, 'APLICAÇÃO PAROU! \n ' + str(datetime.datetime.now()))
        time.sleep(10)
        sys.exit()



func = (2, 5, 7, 18, 19, 21, 30, 35, 37, 50, 51)
def isnoc(id):
    for id_func in func:
        if id_func == id:
            return 'yes'

    return 'no'
'''' 
2 - jvilar
5 - epinheiro
7 - fmonteiro
18 - crodrigues
19 - clima
21 - iuchoa
30 - fzanella
35 - mmarcondes
37 - mlima
50 - pdamaceno
51 - asilva
'''



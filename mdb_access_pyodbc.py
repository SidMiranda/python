import pyodbc


con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\BANCO\att2000.mdb')

cursor = con.cursor()
cursor.execute('SELECT * FROM CHECKINOUT WHERE USERID = 36 ORDER BY CHECKTIME DESC')

for row in cursor.fetchall():

    print(row)

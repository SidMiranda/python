import xlsxwriter
import firebirdsql
import datetime

nMes = datetime.datetime.now()
if nMes.month == 1:
    dt_final = '31-jan-2020'
elif nMes.month == 2:
    dt_final = '28-feb-2020'
elif nMes.month == 3:
    dt_final = '31-mar-2020'
elif nMes.month == 4:
    dt_final = '30-apr-2020'
elif nMes.month == 5:
    dt_final = '31-may-2020'
elif nMes.month == 6:
    dt_final = '30-jun-2020'
elif nMes.month == 7:
    dt_final = '31-jul-2020'
elif nMes.month == 8:
    dt_final = '30-aug-2020'
elif nMes.month == 9:
    dt_final = '31-sep-2020'
elif nMes.month == 10:
    dt_final = '30-oct-2020'
elif nMes.month == 11:
    dt_final = '31-nov-2020'
else:
    dt_final = '30-dec-2020'

dt_inicial = '01-' + dt_final[3:6] + '-2020'

print(dt_inicial)
print(dt_final)

con = firebirdsql.connect(host='localhost', database='C:\\vivo\\FD.GDB', user='SYSDBA', password='masterkey')
cursor1 = con.cursor()
cursor2 = con.cursor()
cursor3 = con.cursor()

print('Cursor aberto')

cursor1.execute('SELECT DISTINCT SERVICOS.CODIG_OCS FROM SERVICOS WHERE SERVICOS.MENSG_OCS like ?', ('%MINUTOS%',))

result = cursor1.fetchall()
print('result OK')
index = 0
codig_ocs = []
for cod in result:
    codig_ocs.append(str(result[index])[2:7])
    index += 1

cursor1.close()
print('Cursor 1 fechado OK')
del(codig_ocs[0])

def Detalha_27(nome_tabela):
    command1 = ('SELECT ' +
    'CONTARESUMO.ddd, CONTARESUMO.NROTELEFO, CONTARESUMO.VALORASSI, CONTARESUMO.DTVENCIME, ' +
    'coalesce(sum(BILHETACAO.DURAC_LIG),0) MINUTOS_TOTAL, ' +
    'coalesce(sum(BILHETACAO.VAL_LIGAC),0) VALOR_TOTAL, ' +
    '(select coalesce(sum(BILHETACAO.DURAC_LIG),0) from BILHETACAO where BILHETACAO.NROTELEFO = CONTARESUMO.NROTELEFO and BILHETACAO.CATEGORIA=? and BILHETACAO.DTVENC_BI BETWEEN ? AND ? ) MINUTOS_VOZ, ' +
    '(select coalesce(sum(BILHETACAO.VAL_LIGAC),0) from BILHETACAO where BILHETACAO.NROTELEFO = CONTARESUMO.NROTELEFO and BILHETACAO.CATEGORIA=? and BILHETACAO.DTVENC_BI BETWEEN ? AND ?) VALOR_VOZ, ' +
    '(select coalesce(sum(BILHETACAO.DURAC_LIG),0) from BILHETACAO where BILHETACAO.NROTELEFO = CONTARESUMO.NROTELEFO and BILHETACAO.CATEGORIA!=? and BILHETACAO.DTVENC_BI BETWEEN ? AND ?) MINUTOS_OUTROS, ' +
    '(select coalesce(sum(BILHETACAO.VAL_LIGAC),0) from BILHETACAO where BILHETACAO.NROTELEFO = CONTARESUMO.NROTELEFO and BILHETACAO.CATEGORIA!=? and BILHETACAO.DTVENC_BI BETWEEN ? AND ?) VALOR_OUTROS, ' +
    '(select coalesce(sum(DESCONTOS.VAL_LIGAC),0) from DESCONTOS where DESCONTOS.NROTELEFO = CONTARESUMO.NROTELEFO and descontos.DTVENC_DE BETWEEN ? AND ?) DESCONTO, ' +
    '(select coalesce(sum(SERVICOS.VAL_LIGAC),0) from SERVICOS where SERVICOS.NROTELEFO = CONTARESUMO.NROTELEFO and SERVICOS.DTVENC_SE BETWEEN ? AND ?) OUTROS_SERV, ')

    command2 = ' '
    for cod in codig_ocs:
        command2 = command2 + '\n(select FIRST 1 coalesce(SERVICOS.MENSG_OCS,0) from SERVICOS where SERVICOS.NROTELEFO = CONTARESUMO.NROTELEFO and SERVICOS.CODIG_OCS=' + cod + ' and SERVICOS.DTVENC_SE BETWEEN ? AND ?) MSG_' + cod + ', '

    for cod in codig_ocs:
            command2 = command2 + '\n(select FIRST 1 coalesce(SERVICOS.VAL_LIGAC,0) from SERVICOS where SERVICOS.NROTELEFO = CONTARESUMO.NROTELEFO and SERVICOS.CODIG_OCS=' + cod + ' and SERVICOS.DTVENC_SE BETWEEN ? AND ?) VAL_' + cod + ', '

    command3 = (' ' +
    # -- Calcula o total a pagar
    'coalesce(sum(BILHETACAO.VAL_LIGAC),0) + CONTARESUMO.VALORASSI + ' +
    '+ (select coalesce(sum(SERVICOS.VAL_LIGAC),0) from SERVICOS where SERVICOS.NROTELEFO = CONTARESUMO.NROTELEFO and SERVICOS.DTVENC_SE BETWEEN ? AND ?) ' +
    '+ (select coalesce(sum(DESCONTOS.VAL_LIGAC),0) from DESCONTOS where DESCONTOS.NROTELEFO = CONTARESUMO.NROTELEFO and descontos.DTVENC_DE BETWEEN ? AND ?) A_PAGAR ')

    command4 = (' from ' +
    '  CONTARESUMO ' +
    ' left join ' +
    '  BILHETACAO on BILHETACAO.NROTELEFO=CONTARESUMO.NROTELEFO ' +
    '  AND CONTARESUMO.DTVENCIME=bilhetacao.DTVENC_BI ' +
    ' AND CONTARESUMO.DTVENCIME BETWEEN ? AND ? ' +
    ' where  ' +
    ' CONTARESUMO.DTVENCIME BETWEEN ? AND ? ' +
    ' group by ' +
    '  CONTARESUMO.ddd, CONTARESUMO.NROTELEFO, CONTARESUMO.VALORASSI, CONTARESUMO.DTVENCIME')

    param = []

    voz = 1
    while voz <= 4:
        param.append("VOZ")
        param.append(dt_inicial)
        param.append(dt_final)
        voz += 1

    for cod in codig_ocs:
        param.append(dt_inicial)
        param.append(dt_final)
        param.append(dt_inicial)
        param.append(dt_final)

    par = 1
    while par <= 6:
        param.append(dt_inicial)
        param.append(dt_final)
        par += 1

    for p in param:
        print(p)

    cursor2.execute(command1 + command2 + command3 + command4, param)
    print('cursores executados')
    header = [row[0] for row in cursor2.description]
    rows = cursor2.fetchall()
    cursor2.close()
    return header, rows


def Durac_Lig(nome_tabela):
    cursor3.execute('SELECT distinct DURAC_LIG, count (DURAC_LIG) ' +
	' from bilhetacao where DTVENC_BI BETWEEN ? AND ? and ' +
    '    (DURAC_LIG >= 0.5) and (DURAC_LIG <= 3) group by DURAC_LIG;', (dt_inicial, dt_final))
    print('Durac_Lig')
    header = [row[0] for row in cursor3.description]
    rows = cursor3.fetchall()
    cursor3.close()
    return header, rows


def export(nome_tabela):
    workbook = xlsxwriter.Workbook(nome_tabela + '.xlsx')
    worksheet1 = workbook.add_worksheet('Detalhamento_27')
    worksheet2 = workbook.add_worksheet('Durac_Lig')
    worksheet3 = workbook.add_worksheet('Grafic')

    header1, rows1 = Detalha_27(nome_tabela)

    row_index = 0
    column_index = 0
    print('Export for 1')
    for column_name in header1:
        worksheet1.write(row_index, column_index, column_name)
        column_index += 1
        print('1')
    row_index += 1

    print('Export for 2')
    for row in rows1:
        column_index = 0
        for column in row:
            worksheet1.write(row_index, column_index, column)
            column_index += 1
        row_index += 1

    print(str(row_index) + ' rows written successfully to ' + workbook.filename)

    header2, rows2 = Durac_Lig(nome_tabela)
    print('Here Ok 2')
    row2_index = 0
    column2_index = 0

    for column_name in header2:
        worksheet2.write(row2_index, column2_index, column_name)
        column2_index += 1

    row2_index += 1
    print('Here Ok 3')
    for row in rows2:
        column2_index = 0
        for column in row:
            worksheet2.write(row2_index, column2_index, column)
            column2_index += 1
        row2_index += 1

    print(str(row2_index) + ' rows written successfully to ' + workbook.filename)

    workbook.close()
    print('workbook closed')
nome = dt_inicial + ' a ' + dt_final
export(nome)


'''
cur.execute('SELECT DISTINCT BILHETACAO.CATEGORIA ' +
' FROM BILHETACAO ' +
' WHERE BILHETACAO.DTVENC_BI BETWEEN ? AND ?', (dt_inicial, dt_final))
'''

'''
cur.execute('SELECT sum(BILHETACAO.DURAC_LIG) MINUTOS, sum(BILHETACAO.VAL_LIGAC) VALOR ' +
' FROM BILHETACAO ' +
' WHERE BILHETACAO.CATEGORIA=? ' +
' AND BILHETACAO.DTVENC_BI BETWEEN ? AND ? ', ('VOZ', dt_inicial, dt_final))
'''

#pprint.pprint(cur.fetchall())



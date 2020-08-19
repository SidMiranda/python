import json

LTime = datetime.datetime.now()
t1 = str(LTime)[:10]
h1 = str(LTime)[11:13]

WTime = requests.get('http://worldtimeapi.org/api/ip/8.8.8.8')
j = json.loads(WTime.content)
t2 = j['datetime'][:10]
h2 = j['datetime'][11:13]

dif = int(h2) - int(h1)

if t1 == t2:
    if (dif > 0) and (dif < 4):
        print('HORA ESTA CORRETA')
    elif (dif < 0) and (dif > -4):
        print('HORA ESTA CORRETA')
    else:
        print('HORA ERRADA')
else:
    print('DATA ERRADA')

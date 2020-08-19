import sched
import time
from datetime import datetime, timedelta

scheduler = sched.scheduler()

def saytime():
    print(time.ctime())
    scheduler.enter(delay=5, priority=0, action=saytime)

saytime()

scheduler.run(blocking=True)
# #Cria uma thred e não espera para continuar rodando o programa

#print(datetime.now().replace(second=0, microsecond=0))
#print(datetime.now().replace(second=0, microsecond=0) + timedelta(hours=5))
#print(datetime.now().replace(second=0, microsecond=0))

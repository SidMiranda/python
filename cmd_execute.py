from subprocess import run, PIPE, STDOUT

comando = run('hostname', shell=True, stdout=PIPE, stderr=STDOUT)
resposta = comando.stdout.decode('cp1252', errors='ignore')

print(resposta)

"""
run('notepad', shell=True)
run('ping google.com.br -t', shell=True)
run('dir', shell=True)
run('cd c:', shell=True)
"""

from bottle import Bottle, request

app = Bottle()

@app.route('/hello')
def hello():
    client_ip = request.environ.get('REMOTE_ADDR')
    print(client_ip)
    return ['<h1 style="color:red">' + client_ip + '</h1>']


app.run(host='IP_Host_Local', port='8080')

from bottle import run, request, get, post

@get('/')
def index_get():
  return '''
  <form action="/" method="post">
    username: <input name="username" type="text" />
    <br>
    password: <input name="password" type="password" />
    <br>
    <input value="Login" type="submit" />
  </form>'''
  
@post('/')
def index_post():
  username = request.forms.get('username')
  password = request.forms.get('password')
  return '''
    <h3> Nome {} <br>
         Senha {}
    '''.format(usernamet, password)
    
run(port=8090)

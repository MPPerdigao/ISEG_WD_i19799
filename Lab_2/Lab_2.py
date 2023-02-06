from flask import Flask, request, redirect, url_for, make_response
app = Flask(__name__)

@app.route('/') 
def main_index():
    return 'Hello World!'

@app.route('/users/<username>') 
def show_user(username):
    return f'User: {username}'

@app.route('/login', methods=['GET', 'POST']) 
def login ():
    if request.method =='POST':
        username= request.form ['username'] 
        return redirect (url_for ('show_user', username= username))
    else:
        username= request.args.get ('password')
        return redirect (url_for ('show_user', username=username))
    
from flask import make_response

@app.route('/')
def index ():
    response = make_response('Hello World!') 
    response.headers['Content-Type'] = 'text/plain' 
    return response


if __name__ == "__main__":
    app.run()

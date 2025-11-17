from flask import Flask, render_template
from flask import request 

app = Flask(__name__)

@app.get('/')
def home():
    teste = request 
    a = 10 
    b = 20  
    c = a + b
    return f"A soma é {c}"

@app.get('/login')
def login():
    return render_template('login.html')


@app.get('/login')
def realizar_login():
    email = request.form.get('email')
    password = request.form.get('password')
    return f"Email: {email}, Password: {password}"

if __name__ == '__main__':
    app.run(debug=True)

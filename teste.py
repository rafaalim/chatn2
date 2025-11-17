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

if __name__ == '_main_':
    app.run(debug=True)

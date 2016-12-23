# coding=utf-8
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Ciao Mondo</h1> <h2>Sottotitolo</h2>'

@app.route('/test')
def test():
    return '<h1>Questo è un test</h1>'

app.run()

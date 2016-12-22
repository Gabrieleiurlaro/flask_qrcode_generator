# coding=utf-8
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Ciao Mondo'

@app.route('/test')
def test():
    return '<h1>Questo è un test</h1>'

app.run()

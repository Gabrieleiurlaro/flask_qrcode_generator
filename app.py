# coding=utf-8
from flask import Flask, request

import cStringIO
import qrcode
from flask import send_file


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Ciao Mondo</h1> <h2>Sottotitolo</h2>'

@app.route('/test')
def test():
    return '<h1>Questo è un test</h1>'

@app.route('/ciaocode')
def ciao_code():
    img_buf = cStringIO.StringIO()
    img = qrcode.make('ciao')
    img.save(img_buf)
    img_buf.seek(0)
    return send_file(img_buf, mimetype='image/png')

@app.route('/qrcode/<value>')
def gen_code_from_dynamic_url(value):
    img_buf = cStringIO.StringIO()
    img = qrcode.make(value)
    img.save(img_buf)
    img_buf.seek(0)
    return send_file(img_buf, mimetype='image/png')


@app.route('/qrcode')
def gen_code_from_get_request():
    value = request.args.get('qrcode')
    img_buf = cStringIO.StringIO()
    img = qrcode.make(value)
    img.save(img_buf)
    img_buf.seek(0)
    return send_file(img_buf, mimetype='image/png')

app.run()

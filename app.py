# coding=utf-8
from flask import Flask, request, render_template, send_file
from flask_bootstrap import Bootstrap

import cStringIO
import qrcode



app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

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

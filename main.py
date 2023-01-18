import os
from flask import Flask, request,render_template
import pathlib
import json
import cv2
import flask
import numpy as np
from Sort import Sort
app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく

# http://127.0.0.1:5000/
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/output', methods=["POST"])
def output():
    r = request.form.get("colorvalue_R")
    if not r:
        r = 0
    g = request.form.get("colorvalue_G")
    if not g:
        g = 0
    b = request.form.get("colorvalue_B")
    if not b:
        b = 0
    #取得したRGBを引数として一番近い画像のパスを取得
    Sort(r,g,b)
    with open('./Data/data.json') as f:
        jsn = json.load(f)
    ps = jsn["path"]
    return render_template("output.html",r=r,g=g,b=b,img=ps)

# アップロード機能
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in flask.request.files:
        return 'ファイル未指定'

    # fileの取得（FileStorage型で取れる）
    # https://tedboy.github.io/flask/generated/generated/werkzeug.FileStorage.html
    fs = flask.request.files['file']

    # 下記のような情報がFileStorageからは取れる
    app.logger.info('file_name={}'.format(fs.filename))
    app.logger.info('content_type={} content_length={}, mimetype={}, mimetype_params={}'.format(
        fs.content_type, fs.content_length, fs.mimetype, fs.mimetype_params))

    # ファイルを保存
    fs.save(os.path.join('./static/images', fs.filename))
    return render_template("index.html")

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)

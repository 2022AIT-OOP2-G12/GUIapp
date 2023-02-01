import os
import secrets
from flask import Flask, request,render_template, flash
import pathlib
import json
import cv2
import flask
import numpy as np
import glob
from base import Base
from base_sort import Base_Sort
app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく
secret = secrets.token_urlsafe(32)
app.secret_key = secret

# http://127.0.0.1:5000/
@app.route('/')
def index():
    flash('')
    Base()
    return render_template("index.html")

@app.route('/back')
def back():
    flash('')
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
    Base_Sort(r,g,b)
    with open('./Data/data_out.json') as f:
        jsn = json.load(f)
    ps = jsn["path"]
    return render_template("output.html",r=r,g=g,b=b,img=ps)

# アップロード機能
@app.route('/upload', methods=['POST'])
def upload():
    
    # fileの取得（FileStorage型で取れる）
    # https://tedboy.github.io/flask/generated/generated/werkzeug.FileStorage.html
    fs = flask.request.files['file']

    if fs.filename == '':
        flash('ファイルがありません')
        return render_template("index.html")

    # 下記のような情報がFileStorageからは取れる
    app.logger.info('file_name={}'.format(fs.filename))
    app.logger.info('content_type={} content_length={}, mimetype={}, mimetype_params={}'.format(
        fs.content_type, fs.content_length, fs.mimetype, fs.mimetype_params))

    # ファイルを保存
    if fs.filename != '':
        fs.save(os.path.join('./static/images', fs.filename))
        Base()
        flash('アップロード完了')

    return render_template("index.html")


@app.route('/uploaded_list/')
def uploaded_list():
    files = glob.glob("./static/images/*")
    urls = []
    for file in files:
        urls.append({
            "filename": os.path.basename(file),
            "url": "/static/images/" + os.path.basename(file)
        })
    return render_template("saved_image.html", page_title="アップロードファイル", target_files=urls)

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True,port=8888)

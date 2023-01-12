from flask import Flask, request,render_template
import pathlib
import json
import cv2
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

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)

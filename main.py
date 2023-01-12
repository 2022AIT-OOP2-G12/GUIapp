from flask import Flask, render_template
import pathlib
import json
app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく

# http://127.0.0.1:5000/
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/outout')
def upload():
    with open('./Data/data.json') as f:
        jsn = json.load(f)
    ps = jsn["path"]
    img = out_img(ps)
    return render_template("output.html",img)

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)

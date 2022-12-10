"""
Powershell
$env:FLASK_APP = "111flask.py"
FLask run
set FLASK_APP=111flask.py
flask run
"""

from flask import Flask, render_template
from flask_cors import CORS #本地開發時 跨域
import json


app = Flask(__name__) #__name__代表此檔案
CORS(app)

@app.route('/') #裝飾:以函式為基礎，提供附加功能 沒很懂
def index():
    return render_template("111index.html")

@app.route('/<flooding_risk>/<detail>')
def paging(flooding_risk, detail):
    return render_template(detail)
    

if __name__ == "__main__": #以主程式執行才執行
    app.run()


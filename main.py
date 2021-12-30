#!flask/bin/python
# -- coding: utf-8 --

__author__ = 'cloudtogo'

from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello():
    return '恭喜您成功地发布了一个运行在云端的python-public程序，公网github,branch1分支'
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=81)

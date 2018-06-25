from flask import Flask
from flask import url_for
import os

app = Flask(__name__)

@app.route('/')
def hello():
    print(url_for('toOpen', id='2'))
    return '<h1>Hello,World!</h1><a href="http://127.0.0.1:5000/open/2">点击这里</a>'

@app.route('/open/<id>/')
def toOpen(id):
    return '打开的是id为%s的文章' % id

if __name__ == '__main__':
    app.run(debug=True)
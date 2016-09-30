#!/usr/bin/env python3
#-*- coding: utf-8 -*- 

# flash web app demo

from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
	return '<h1>home</h1>'


@app.route('/sigin',methods=['GET'])
def sigin_form():
	return '''<form action="/sigin" method="post">
			<p><input type="text" name="username"></p>
			<p><input type="password" name="password"></p>
			<p><button type="submit">submit</button></p>
			</form>'''


@app.route('/sigin',methods=['POST'])
def sigin():
	username = request.form['username']
	password = request.form['password']
	if username == 'admin' and password == 'admin':
		return '<h3>hello,admin</h3>'
	return '<h3>Bad username or password!</h3>'


if __name__ == '__main__':
	app.run()
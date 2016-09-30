# server.py created by liaozq 2016/09/30
# 从wsgiref 导入
from wsgiref.simple_server import make_server
# 从hello.py导入
from hello import application


if __name__ == '__main__':
	httpd = make_server('',8000,application)
	print('Server HTTP listening 8000.....')
	httpd.serve_forever()
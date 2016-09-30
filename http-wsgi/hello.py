# created by liaozq 2016/09/30


def application(envision,start_response):
	start_response('200 OK',[('Content-Type','text/html')])
	return [b'<ht1>hello,web!</h1>']

from wsgiref.simple_server import make_server

def web_app(environment, response):
	status = "200 OK"
	headers = [('Content-type', 'text/html; charset=utf-8')]
	response(status,headers)

	return [b'Hello World']



with make_server('', 8000, web_app) as server:
	print("Serving on port 8000...\n visit http://127.0.0.1:8000\n to kill server enter ctrl+c")

	server.serve_forever()
	
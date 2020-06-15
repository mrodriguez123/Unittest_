import unittest, pytest
from wsgiref.simple_server import make_server
import app
import urllib.request as urllib2

class TestMain(unittest.TestCase):

	with make_server('', 8000, web_app) as server:
		def test_web_app(self):
			self.assertEqual(app.status_code, 200)


if __name__ == '__main__':
	unittest.main()

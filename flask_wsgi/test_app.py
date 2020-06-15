import unittest, pytest
from wsgiref.simple_server import make_server
import app
from flask import Flask
from flask_testing import TestCase, LiveServerTestCase
import urllib.request as urllib2

class MyTest(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app
class MyTest(LiveServerTestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True

        # Set to 0 to have the OS pick the port.
        app.config['LIVESERVER_PORT'] = 0

        return app

    def test_server_is_up_and_running(self):
        response = urllib2.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)
if __name__ == '__main__':
	unittest.main()

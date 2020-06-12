import unittest, pytest
from flask import Flask, request
import app_json

dictionary= { "name": " Monica",
    	"school": " University of Wisconsin",
    	"sports": " rowing" }

class TestMain(unittest.TestCase):

	def test_index_post(self):
    		app = Flask(__name__)
    		client = app.test_client()
    		url = '/'
    		response= client.get(url)

    		self.assertEqual(response.get_data(), b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML[193 chars]p>\n' )
    		self.assertEqual(response.status_code, 200)

	def test_index_get(self):
			app = Flask(__name__)
			client = app_json.test_client()
			url = '/get'
			response= client.get(url) 

			self.assertEqual(response.get_data(),{"key":[0,1,2,3]})
			self.assertEqual(response.status_code, 200)

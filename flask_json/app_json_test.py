import unittest, pytest
from flask import Flask, request
import app_json
import urllib.request as urllib2


dictionary= { "name": " Monica",
    	"school": " University of Wisconsin",
    	"sports": " rowing" }

class TestMain(unittest.TestCase):

	def test_index_post(self):
			app = Flask(__name__)
			response = self.cleint.get('/post') 
			self.assertEquals(response.json, dict(success=True))


	def test_index_get(self):
			app = Flask(__name__)
			response = self.cleint.get('/get') 
			self.assertEquals(response.json, dict(success=True))

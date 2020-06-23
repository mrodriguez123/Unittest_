import unittest
from app import app

dictionary= { "name": " Monica",
    	"school": " University of Wisconsin",
    	"sports": " rowing" }

class FlaskTestCase(unittest.TestCase):

    # Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to my page', response.data)

    def test_get(self):
    	tester = app.test_client(self)
    	response = tester.get('/get', content_type='json')
    	self.assertEqual(response.status_code, 200)
    	self.assertEqual(response.json, dict(nums = [0,1,2,3]))



if __name__ == '__main__':
    unittest.main()

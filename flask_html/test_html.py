from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_index_msg(self):
    	tester = app.test_client(self)
    	response = tester.get('/')
    	self.assertIn(b'Hello World', response.data)

    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/home', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        tester = app.test_client(self)
        response = tester.get('/about', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    def test_about_msg(self):
    	tester = app.test_client(self)
    	response = tester.get('/about')
    	self.assertIn(b'About Page', response.data)

if __name__ == '__main__':
    unittest.main()

import html_post
import unittest
import pytest

class TestMain(unittest.TestCase):
    def test_post_text(self):
        self.assertEqual(html_post.post_text(), {'name': 'Moni', 'school': 'University of Wisconsin'}) 


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False) 
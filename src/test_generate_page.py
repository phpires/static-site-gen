import unittest
from generate_page import extract_title
class TestGeneratePage(unittest.TestCase):
    def test_generate_page(self):
        md = "#   Header h1   "
        title = extract_title(md)
        self.assertEqual(title, "Header h1")
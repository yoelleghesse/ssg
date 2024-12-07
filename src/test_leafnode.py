import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_no_value(self):
        node = LeafNode(tag='p', value =None, props={'href': "https://www.google.com"})
        with self.assertRaises(ValueError):
            node.to_html()

    def test_valid_leafnode(self):
        node = LeafNode(tag='a', value='Click me!', props={'href': "https://www.google.com"})
        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected)

    def test_raw_text(self):
        node = LeafNode(tag=None, value="raw text")
        expected = "raw text"
        self.assertEqual(node.to_html(), expected)

    def test_no_props(self):
        node = LeafNode(tag='p', value='no props')
        expected = f"<{'p'}>{'no props'}</{'p'}>"
        self.assertEqual(node.to_html(), expected)

if __name__ == "__main__":
    unittest.main()
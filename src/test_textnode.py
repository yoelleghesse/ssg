import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_different_type(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.ITALIC_TEXT)
        self.assertNotEqual(node, node2)

    def test_different_text(self):
        node = TextNode("This is text 1", TextType.BOLD_TEXT)
        node2 = TextNode("This is text 2", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url_none(self):
    # Test equality when url is None in both nodes
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT, url=None)
        self.assertEqual(node, node2)

    def test_not_eq_one_url_none(self):
        # Test inequality when url is None in one node but not the other
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT, url="https://example.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()

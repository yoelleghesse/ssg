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

    def test_invalid_text_type(self):
        text_node = TextNode(text="Sample text", text_type="invalid", url=None)
        with self.assertRaises(ValueError):
            TextNode.text_node_to_html_node(text_node)

    def test_split_delimiter_code(self):
        old_nodes = [TextNode("This is text with a `code block` word", TextType.NORMAL_TEXT)]
        new_nodes = TextNode.split_nodes_delimiter(old_nodes, "`", TextType.CODE_TEXT)
        expected = [
            TextNode("This is text with a ", TextType.NORMAL_TEXT),
            TextNode("code block", TextType.CODE_TEXT),
            TextNode(" word", TextType.NORMAL_TEXT)
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_delimiter_bold(self):
        old_nodes = [TextNode("This is text with a **bold word**", TextType.NORMAL_TEXT)]
        new_nodes = TextNode.split_nodes_delimiter(old_nodes, "**", TextType.BOLD_TEXT)
        expected = [
            TextNode("This is text with a ", TextType.NORMAL_TEXT),
            TextNode("bold word", TextType.BOLD_TEXT),
            TextNode("", TextType.NORMAL_TEXT)
        ]
        self.assertEqual(new_nodes, expected)
        
    def test_split_delimiter_italic(self):
        old_nodes = [TextNode("This is text with a *italic word*", TextType.NORMAL_TEXT)]
        new_nodes = TextNode.split_nodes_delimiter(old_nodes, "*", TextType.ITALIC_TEXT)
        expected = [
            TextNode("This is text with a ", TextType.NORMAL_TEXT),
            TextNode("italic word", TextType.ITALIC_TEXT),
            TextNode("", TextType.NORMAL_TEXT)
        ]
        self.assertEqual(new_nodes, expected)
                              

if __name__ == "__main__":
    unittest.main()

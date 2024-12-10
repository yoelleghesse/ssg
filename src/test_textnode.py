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

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        match = TextNode.extract_markdown_images(text)
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(match, expected)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        match = TextNode.extract_markdown_links(text)
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(match, expected)
                              
    def test_split_nodes_link(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",TextType.NORMAL_TEXT)
        expected = [
            TextNode("This is text with a link ", TextType.NORMAL_TEXT),
            TextNode("to boot dev", TextType.LINK_TEXT, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL_TEXT),
            TextNode("to youtube", TextType.LINK_TEXT, "https://www.youtube.com/@bootdotdev")
            ]
        self.assertEqual(TextNode.split_nodes_link([node]), expected)

    def test_split_nodes_image(self):
        node = TextNode("This is text with an image ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",TextType.NORMAL_TEXT)
        expected = [
            TextNode("This is text with an image ", TextType.NORMAL_TEXT),
            TextNode("rick roll", TextType.IMAGE_TEXT, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.NORMAL_TEXT),
            TextNode("obi wan", TextType.IMAGE_TEXT, "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        self.assertEqual(TextNode.split_nodes_image([node]), expected)


    



if __name__ == "__main__":
    unittest.main()

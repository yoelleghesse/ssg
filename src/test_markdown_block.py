import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type, block_to_html_node, markdown_to_html, text_to_children, HTMLNode

class TestMarkdownToHTML(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )


    def test_block_to_block_type_heading(self):
        self.assertEqual(block_to_block_type("# Heading"), "heading")

    def test_block_to_block_type_ordered_list(self):
        self.assertEqual(block_to_block_type("1. First item\n2. Second item"), "ordered_list")

    def test_block_to_block_type_unordered_list(self):
        self.assertEqual(block_to_block_type("* First item\n* Second item"), "unordered_list")

    def test_block_to_block_type_quote(self):
        self.assertEqual(block_to_block_type("> This is a quote"), "quote")
    
    def test_block_to_block_type_code(self):
        self.assertEqual(block_to_block_type("```\nThis is a code block\n```"), "code")

    def test_block_to_html_node_heading(self):
        block = "# Heading"
        expected = HTMLNode("<h1>", "", [HTMLNode("", "Heading", [], {})], {})
        self.assertEqual(block_to_html_node(block), expected)

    def test_block_to_html_node_ordered_list(self):
        block = "1. First item\n2. Second item"
        expected = HTMLNode("<ol>", "", [
            HTMLNode("<li>", "", [HTMLNode("", "First item", [], {})], {}),
            HTMLNode("<li>", "", [HTMLNode("", "Second item", [], {})], {})
        ], {})
        self.assertEqual(block_to_html_node(block), expected)

    def test_block_to_html_node_unordered_list(self):
        block = "* First item\n* Second item"
        expected = HTMLNode("<ul>", "", [
            HTMLNode("<li>", "", [HTMLNode("", "First item", [], {})], {}),
            HTMLNode("<li>", "", [HTMLNode("", "Second item", [], {})], {})
        ], {})
        self.assertEqual(block_to_html_node(block), expected)

    def test_block_to_html_node_quote(self):
        block = "> This is a quote"
        expected = HTMLNode("<blockquote>", "", [HTMLNode("", "This is a quote", [], {})], {})
        self.assertEqual(block_to_html_node(block), expected)

    def test_block_to_html_node_code(self):
        block = "```\nprint('Hello, world!')\n```"
        expected = HTMLNode("<pre>", "", [
            HTMLNode("<code>", "", [HTMLNode("", "print('Hello, world!')", [], {})], {})
        ], {})
        self.assertEqual(block_to_html_node(block), expected)

    def test_markdown_to_html(self):
        markdown = "# Heading\n\n1. First item\n2. Second item\n\n* Unordered item\n\n> Quote\n\n```\nprint('Hello, world!')\n```"
        expected = HTMLNode("<div>", "", [
            HTMLNode("<h1>", "", [HTMLNode("", "Heading", [], {})], {}),
            HTMLNode("<ol>", "", [
                HTMLNode("<li>", "", [HTMLNode("", "First item", [], {})], {}),
                HTMLNode("<li>", "", [HTMLNode("", "Second item", [], {})], {})
            ], {}),
            HTMLNode("<ul>", "", [
                HTMLNode("<li>", "", [HTMLNode("", "Unordered item", [], {})], {})
            ], {}),
            HTMLNode("<blockquote>", "", [HTMLNode("", "Quote", [], {})], {}),
            HTMLNode("<pre>", "", [
                HTMLNode("<code>", "", [HTMLNode("", "print('Hello, world!')", [], {})], {})
            ], {})
        ], {})
    
        self.assertEqual(markdown_to_html(markdown), expected)
    

if __name__ == "__main__":
    unittest.main()

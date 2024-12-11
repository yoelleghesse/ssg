import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type

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
        

if __name__ == "__main__":
    unittest.main()

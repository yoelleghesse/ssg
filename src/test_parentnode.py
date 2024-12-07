import unittest
from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
    def test_parent_node_no_children(self):
        parent = ParentNode(tag="div", children=[])
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_parent_node_multiple_children(self):
        child1 = LeafNode(tag="p", value="This is a paragraph.")
        child2 = LeafNode(tag="a", value="Click here!", props={"href": "https://www.example.com"})
        parent = ParentNode(tag="div", children=[child1, child2])
        expected = (
            "<div>"
            "<p>This is a paragraph.</p>"
            "<a href=\"https://www.example.com\">Click here!</a>"
            "</div>"
        )
        self.assertEqual(parent.to_html(), expected)

    def test_parent_node_with_nested_parent_node(self):
        child1 = LeafNode(tag="p", value='This is a paragraph.')
        child2 = ParentNode(tag="section", children=[LeafNode(tag="h2", value="Header")])
        parent = ParentNode(tag="div", children=[child1, child2])
        expected = (
            "<div>"
            "<p>This is a paragraph.</p>"
            "<section><h2>Header</h2></section>"
            "</div>"
        )
        self.assertEqual(parent.to_html(), expected)

    def test_parent_node_no_props(self):
        child1 = LeafNode(tag="p", value="This is a paragraph.")
        parent = ParentNode(tag="div", children=[child1])
        expected = "<div><p>This is a paragraph.</p></div>"
        self.assertEqual(parent.to_html(), expected)
    
    def test_parent_node_with_props(self):
        child1 = LeafNode(tag="p", value="This is a paragraph.")
        parent = ParentNode(tag="div", children=[child1], props={"class": "container"})
        expected = "<div class=\"container\"><p>This is a paragraph.</p></div>"
        self.assertEqual(parent.to_html(), expected) 

    def test_parent_node_empty_tag(self):
        child = LeafNode(tag="p", value="This is a paragraph.")
        parent = ParentNode(tag="", children=[child])
        expected = "<><p>This is a paragraph.</p></>"
        self.assertEqual(parent.to_html(), expected)

if __name__ == "__main__":
    unittest.main()
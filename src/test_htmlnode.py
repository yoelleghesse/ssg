import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_minimal_node(self):
        node = HTMLNode(tag="div")
        expected = "HTMLNode(tag='div', value=None, children=[], props='')"
        assert repr(node) == expected

    def test_node_with_value(self):
        node = HTMLNode(tag="p", value="This is text")
        expected = "HTMLNode(tag='p', value='This is text', children=[], props='')"
        assert repr(node) == expected

    def test_node_with_children(self):
        child1 = HTMLNode(tag="p", value="Paragraph 1")
        child2 = HTMLNode(tag="p", value="Paragraph 2")
        parent = HTMLNode(tag="div", children=[child1, child2])
        expected = (
            "HTMLNode(tag='div', value=None, children=["
            "HTMLNode(tag='p', value='Paragraph 1', children=[], props=''), "
            "HTMLNode(tag='p', value='Paragraph 2', children=[], props='')], "
            "props='')"
            )
        assert repr(parent) == expected 

    def test_empty_tag(self):
        node = HTMLNode(tag='', value='empty tag')
        expected = "HTMLNode(tag='', value='empty tag', children=[], props='')"
        assert repr(node) == expected

    def test_node_with_props(self):
        node = HTMLNode(tag='div', props={"href": "https://www.google.com"})
        expected = "HTMLNode(tag='div', value=None, children=[], props='href=\"https://www.google.com\"')"
        assert repr(node) == expected
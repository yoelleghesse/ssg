from enum import Enum
import re
from leafnode import LeafNode

class TextType(Enum):
    NORMAL_TEXT = "normal"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK_TEXT = "link"
    IMAGE_TEXT = "images"

class TextNode:
    def __init__(self, text, text_type: TextType, url= None):
        self.text = text
        self.text_type = text_type
        self.url = url 

    def __eq__(self, value):
        if self.text == value.text:
            if self.text_type.value == value.text_type.value:
                if self.url == value.url:
                    return True
                
    def __repr__(self):
        if self.url:
            return f"TextNode(text='{self.text}', text_type='{self.text_type.value}', url='{self.url}')"
        else:
            return f"TextNode(text='{self.text}', text_type='{self.text_type.value}')"
        
    def text_node_to_html_node(text_node):
        if text_node.text_type == TextType.NORMAL_TEXT:
            return LeafNode(None, text_node.text)
        if text_node.text_type == TextType.BOLD_TEXT:
            return LeafNode("b", text_node.text)
        if text_node.text_type == TextType.ITALIC_TEXT:
            return LeafNode("i", text_node.text)
        if text_node.text_type == TextType.CODE_TEXT:
            return LeafNode("code", text_node.text)
        if text_node.text_type == TextType.LINK_TEXT:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        if text_node.text_type == TextType.IMAGE_TEXT:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        raise ValueError(f"Invalid text type {text_node.text_type}")
    
    def split_nodes_delimiter(old_nodes, delimiter, text_type):
        new_lst = []
        for node in old_nodes:
            if node.text_type == TextType.NORMAL_TEXT:
                parts = node.text.split(delimiter)
                for i, part in enumerate(parts):
                    if i % 2 == 0:
                        new_lst.append(TextNode(part, TextType.NORMAL_TEXT))
                    else:
                        new_lst.append(TextNode(part, text_type))
            else:
                new_lst.append(node)
        return new_lst

    def extract_markdown_images(text):
        return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    def extract_markdown_links(text):
        return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    def split_nodes_link(old_nodes):
        new_nodes = []
        for old_node in old_nodes:
            if old_node.text_type != TextType.NORMAL_TEXT:
                new_nodes.append(old_node)
                continue
            original_text = old_node.text
            links = TextNode.extract_markdown_links(original_text)
            if len(links) == 0:
                new_nodes.append(old_node)
                continue
            for link in links:
                sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
                if len(sections) != 2:
                    raise ValueError("Invalid markdown, link section not closed")
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.NORMAL_TEXT))
                new_nodes.append(TextNode(link[0], TextType.LINK_TEXT, link[1]))
                original_text = sections[1]
            if original_text != "":
                new_nodes.append(TextNode(original_text, TextType.NORMAL_TEXT))
        return new_nodes
    
    def split_nodes_image(old_nodes):
        new_nodes = []
        for old_node in old_nodes:
            if old_node.text_type != TextType.NORMAL_TEXT:
                new_nodes.append(old_node)
                continue
            original_text = old_node.text
            images = TextNode.extract_markdown_images(original_text)
            if len(images) == 0:
                new_nodes.append(old_node)
                continue
            for image in images:
                sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
                if len(sections) != 2:
                    raise ValueError("Invalid markdown, image section not closed")
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.NORMAL_TEXT))
                new_nodes.append(
                    TextNode(
                        image[0],
                        TextType.IMAGE_TEXT,
                        image[1],
                    )
                )
                original_text = sections[1]
            if original_text != "":
                new_nodes.append(TextNode(original_text, TextType.NORMAL_TEXT))
        return new_nodes
    
    def text_to_textnodes(text):
        nodes = [TextNode(text, TextType.NORMAL_TEXT)]
        nodes = TextNode.split_nodes_image(nodes)
        nodes = TextNode.split_nodes_link(nodes)
        
        nodes = TextNode.split_nodes_delimiter(nodes, "**", TextType.BOLD_TEXT)
        nodes = TextNode.split_nodes_delimiter(nodes, "*", TextType.ITALIC_TEXT)
        nodes = TextNode.split_nodes_delimiter(nodes, "`", TextType.CODE_TEXT)

        return nodes

        

    
        

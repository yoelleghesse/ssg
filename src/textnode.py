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
        new_lst = []
        link_pattern = r"\[([^\[\]]+)\]\(([^\(\)]+)\)"
        for node in old_nodes:
            if not isinstance(node, TextNode) or node.text_type != TextType.NORMAL_TEXT:
                new_lst.append(node)
                continue
            parts = re.split(link_pattern, node.text)
            for i in range(len(parts)):
                if i % 3 == 0 and parts[i]:  # Normal text
                    new_lst.append(TextNode(parts[i], TextType.NORMAL_TEXT))
                elif i % 3 == 1:  # Link text
                    link_text = parts[i]
                    url = parts[i + 1] if i + 1 < len(parts) else ""
                    new_lst.append(TextNode(link_text, TextType.LINK_TEXT, url))
        return [node for node in new_lst if node.text]
    
    def split_nodes_image(old_nodes):
        new_lst = []
        image_pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
        for node in old_nodes:
            if not isinstance(node, TextNode) or node.text_type != TextType.NORMAL_TEXT:
                new_lst.append(node)
                continue
            parts = re.split(image_pattern, node.text)
            for i in range(len(parts)):
                if i % 3 == 0 and parts[i]:  # Normal text
                    new_lst.append(TextNode(parts[i], TextType.NORMAL_TEXT))
                elif i % 3 == 1:  # Image alt text
                    alt_text = parts[i]
                    url = parts[i + 1] if i + 1 < len(parts) else ""
                    new_lst.append(TextNode(alt_text, TextType.IMAGE_TEXT, url))
        return [node for node in new_lst if node.text]
        

    
        

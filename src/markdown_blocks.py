from enum import Enum
import re
from leafnode import LeafNode
from textnode import TextNode, TextType
from htmlnode import HTMLNode

def markdown_to_blocks(markdown):
    filtered = []
    markdown = markdown.split("\n\n")
    for mk in markdown:
        filtered.append(mk.strip())
    return filtered


def block_to_block_type(block):
    block = block.strip()
    if block.startswith("* "):
        return "unordered_list"
    if block[0].isdigit() and block[1] == ".":
        return "ordered_list"
    if block.startswith("#"):
        return "heading"
    if block.startswith(">"):
        return "quote"
    if block.startswith("```"):
        return "code"
    else:
        return "paragraph"
    
def block_to_html_node(block):
    block_type = block_to_block_type(block)
    
    if block_type == "heading":
        html_node = HTMLNode(f"<h{block.count('#')}>", "", text_to_children(block.strip("# ").strip()), {})
    elif block_type == "ordered_list":
        html_node = HTMLNode("<ol>", "", [], {})
        list_items = block.split("\n")
        for item in list_items:
            if item.strip():
                li_node = HTMLNode("<li>", "", text_to_children(item[item.index(".") + 1:].strip()), {})
                html_node.children.append(li_node)
    elif block_type == "unordered_list":
        html_node = HTMLNode("<ul>", "", [], {})
        list_items = block.split("\n")
        for item in list_items:
            if item.strip():
                li_node = HTMLNode("<li>", "", text_to_children(item[1:].strip()), {})
                html_node.children.append(li_node)
    elif block_type == "quote":
        html_node = HTMLNode("<blockquote>", "", text_to_children(block[1:].strip()), {})
    elif block_type == "code":
        pre_node = HTMLNode("<pre>", "", [], {})
        code_node = HTMLNode("<code>", "", text_to_children(block.strip("```").strip()), {})
        pre_node.children.append(code_node)
        html_node = pre_node
    else:
        html_node = HTMLNode("<p>", "", text_to_children(block), {})
    return html_node

def text_to_children(text):
    return [HTMLNode("", text, [], {})]

def markdown_to_html(markdown):
    blocks = markdown.split("\n\n")
    parent_node = HTMLNode("<div>", "", [], {})
    for block in blocks:
        html_node = block_to_html_node(block)
        parent_node.children.append(html_node)
    return parent_node

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("# "):
            return block.strip("# ").strip()
    raise Exception("No h1 header found")


    
    


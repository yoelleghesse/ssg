from enum import Enum
import re
from leafnode import LeafNode
from textnode import TextNode, TextType

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
    
    


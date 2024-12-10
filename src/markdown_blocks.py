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

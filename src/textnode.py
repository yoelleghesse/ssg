from enum import Enum

class TextType(Enum):
    NORMAL_TEXT = "normal"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINKS_TEXT = "links"
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

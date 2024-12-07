from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag")
        if len(self.children) == 0:
            raise ValueError("No children")
        children_html = ''.join(child.to_html() for child in self.children)
        props_str = self.props_to_html()
        if props_str:
            return f"<{self.tag} {props_str}>{children_html}</{self.tag}>"
        else:
            return f"<{self.tag}>{children_html}</{self.tag}>"
        

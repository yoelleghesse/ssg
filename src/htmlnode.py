class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children else []
        self.props = props if props else {}

    def to_html(self):
        raise NotImplementedError
    
    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (self.tag == other.tag and
                self.value == other.value and
                self.children == other.children and
                self.props == other.props)

    
    def props_to_html(self):
        return " ".join(f'{key}="{value}"' for key, value in self.props.items()) if self.props else ""
    
    def __repr__(self):
        props_str = self.props_to_html() 
        props_repr = f"'{props_str}'" if props_str else "''"
        return (
            f"HTMLNode("
            f"tag={repr(self.tag)}, "
            f"value={repr(self.value)}, "
            f"children={repr(self.children)}, "
            f"props={props_repr})"
        )
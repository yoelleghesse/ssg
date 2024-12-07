from textnode import TextNode, TextType

def main():

    node = TextNode("This is a text node", TextType.BOLD_TEXT, "https://www.youtube.com")
    print(node)

main()

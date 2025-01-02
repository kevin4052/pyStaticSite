from textnode import *
from htmlnode import *

def main():
    text_node = TextNode("Hello, World!", TextType.LINK, "https://www.example.com")
    html_node = text_node_to_html_node(text_node)
    print(repr(html_node))
    print(html_node.to_html())

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(value=text_node.text)
        case TextType.NORMAL:
            return LeafNode("p", text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError(f"Invalid TextType: {text_node.text_type}")

if __name__ == "__main__":
    main()
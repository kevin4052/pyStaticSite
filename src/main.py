from textnode import *
from htmlnode import *
from utils import *

def main():
    text_node = TextNode("Hello, World!", TextType.TEXT)
    html_node = text_node_to_html_node(text_node)
    print(repr(html_node))
    print(html_node.to_html())

if __name__ == "__main__":
    main()
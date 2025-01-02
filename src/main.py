from textnode import *
from htmlnode import *

def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)
    htmlnode = HTMLNode("div", "This is a div node")
    print(htmlnode)

if __name__ == "__main__":
    main()
from textnode import *
from htmlnode import *
from utils import *

def main():
    node1 = TextNode("`This is text `with a code block word", TextType.TEXT)
    node2 = TextNode("This is text with a `code block` word `second code block`.", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node1, node2], "`", TextType.BOLD)
    print(new_nodes)


if __name__ == "__main__":
    main()
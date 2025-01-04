from textnode import *
from htmlnode import *
from utils import *

def main():
    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    nodes = text_to_textnodes(text)
    for node in nodes:
        print(node)

if __name__ == "__main__":
    main()
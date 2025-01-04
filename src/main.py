from textnode import *
from htmlnode import *
from utils import *

def main():
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print("image: ", extract_markdown_images(text))
    print("link: ", extract_markdown_links(text))

    node = TextNode(text, TextType.TEXT)
    split_node_img = split_nodes_image([node])
    split_node_l = split_nodes_link([node])
    print("split image nodes", len(split_node_img), split_node_img)
    print("split link nodes", len(split_node_l), split_node_l)


if __name__ == "__main__":
    main()
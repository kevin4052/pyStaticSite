from textnode import *
from htmlnode import *
from utils import *

def main():
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print("image: ", extract_markdown_images(text))
    print("link: ", extract_markdown_links(text))
    # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]


if __name__ == "__main__":
    main()
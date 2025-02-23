from textnode import *
from htmlnode import *
from utils import *

def main():
    text = '''   # This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
'''
    blocks = markdown_to_blocks(text)
    for block in blocks:
        print(block)

if __name__ == "__main__":
    main()
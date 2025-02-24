from textnode import *
from htmlnode import *
from utils import *

def main():
    text = '''   # This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item

1. This is the first item in an ordered list
2. This is the second item in an ordered list

```
def testMarkdownToBlocks():
    return True
```
'''
    blocks = markdown_to_blocks(text)
    print(f"Number of blocks: {len(blocks)}")
    for block in blocks:
        print(block_to_block_type(block))

    # test = "> Testing split_nodes_delimiter"
    # test_list = test.split(".", maxsplit=1)
    # print(test_list)
    # print(block_to_block_type(test))

if __name__ == "__main__":
    main()
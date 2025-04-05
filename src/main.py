from textnode import *
from htmlnode import *
from utils import *
from markdown import *

def test_paragraphs(self):
    md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

def test_codeblock(self):
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )

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
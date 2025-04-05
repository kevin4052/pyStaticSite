from utils import *
from block_type_enum import BlockType

def markdown_to_html_node(markdown):
    node = ParentNode()
    node.tag = "div"
    # split the markdown text into blocks
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        match block_to_block_type(block):
            case BlockType.PARAGRAPH:
                node.add_child(LeafNode())
            # case BlockType.HEADING:
            # case BlockType.CODE:
            # case BlockType.QUOTE:
            # case BlockType.UNORDERED_LIST:
            # case BlockType.ORDERED_LIST:
            case _:
                raise ValueError("Unknown block type")
    # returns a parent HTMLNode object
    # parent node contains all the children nodes
    # This function is a placeholder and should be implemented
    pass
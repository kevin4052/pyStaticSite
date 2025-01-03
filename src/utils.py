from textnode import *
from htmlnode import *

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError(f"Invalid TextType: {text_node.text_type}")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    d_len = len(delimiter)
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        remaining_text = node.text
        while True:
            start = remaining_text.find(delimiter)
            if start == -1:
                if remaining_text != "":
                    new_nodes.append(TextNode(remaining_text, TextType.TEXT))
                break

            end = remaining_text.find(delimiter, start + d_len)
            if end == -1:
                raise ValueError(f"Closing delimiter not found: {delimiter}")

            before_delimiter = remaining_text[:start]
            inside_delimiter = remaining_text[start + d_len:end]
            remaining_text = remaining_text[end + d_len:]
            # print(f"start: {start}, end: {end}")
            # print(f"Before: {before_delimiter}, Inside: {inside_delimiter}, Remaining: {remaining_text}")

            if before_delimiter != "":
                new_nodes.append(TextNode(before_delimiter, TextType.TEXT))
            if inside_delimiter != "":
                new_nodes.append(TextNode(inside_delimiter, text_type))
    return new_nodes
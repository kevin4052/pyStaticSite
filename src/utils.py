import re
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

def split_nodes_image(old_nodes):
    nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            nodes.append(node)
            continue

        images = extract_markdown_images(node.text)
        if not images:
            nodes.append(TextNode(node.text, TextType.TEXT))
            continue

        remaining_text = node.text
        for image in images:
            md_text = f"![{image[0]}]({image[1]})"
            sections = remaining_text.split(md_text, 1)
            before_image = sections[0]
            remaining_text = sections[1]

            if before_image != "":
                nodes.append(TextNode(before_image, TextType.TEXT))
            nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))

        if remaining_text != "":
            nodes.append(TextNode(remaining_text, TextType.TEXT))
    return nodes

def split_nodes_link(old_nodes):
    nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            nodes.append(node)
            continue

        links = extract_markdown_links(node.text)
        if not links:
            nodes.append(TextNode(node.text, TextType.TEXT))
            continue

        remaining_text = node.text
        for link in links:
            md_text = f"[{link[0]}]({link[1]})"
            sections = remaining_text.split(md_text, 1)
            before_image = sections[0]
            remaining_text = sections[1]

            if before_image != "":
                nodes.append(TextNode(before_image, TextType.TEXT))
            nodes.append(TextNode(link[0], TextType.LINK, link[1]))

        if remaining_text != "":
            nodes.append(TextNode(remaining_text, TextType.TEXT))
    return nodes

def extract_markdown_images(text):
    regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex, text)
    return matches

def extract_markdown_links(text):
    regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex, text)
    return matches

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
import unittest

from utils import *

class TestUtils_text_node_to_html_node_text(unittest.TestCase):
    def test_text_node_to_html_node_text(self):
        text_node = TextNode("Hello, World!", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(repr(html_node), "HTMLNode(None, Hello, World!, None, None)")
        self.assertEqual(html_node.to_html(), "Hello, World!")

    def test_text_node_to_html_node_bold(self):
        text_node = TextNode("Hello, World!", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(repr(html_node), "HTMLNode(b, Hello, World!, None, None)")
        self.assertEqual(html_node.to_html(), "<b>Hello, World!</b>")

    def test_text_node_to_html_node_italic(self):
        text_node = TextNode("Hello, World!", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(repr(html_node), "HTMLNode(i, Hello, World!, None, None)")
        self.assertEqual(html_node.to_html(), "<i>Hello, World!</i>")

    def test_text_node_to_html_node_code(self):
        text_node = TextNode("Hello, World!", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(repr(html_node), "HTMLNode(code, Hello, World!, None, None)")
        self.assertEqual(html_node.to_html(), "<code>Hello, World!</code>")

    def test_text_node_to_html_node_link(self):
        text_node = TextNode("Hello, World!", TextType.LINK, "https://www.example.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(repr(html_node), "HTMLNode(a, Hello, World!, None, {'href': 'https://www.example.com'})")
        self.assertEqual(html_node.to_html(), '<a href="https://www.example.com">Hello, World!</a>')

    def test_text_node_to_html_node_image(self):
        text_node = TextNode("Hello, World!", TextType.IMAGE, "https://www.example.com/image.png")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(repr(html_node), "HTMLNode(img, , None, {'src': 'https://www.example.com/image.png', 'alt': 'Hello, World!'})")
        self.assertEqual(html_node.to_html(), '<img src="https://www.example.com/image.png" alt="Hello, World!"></img>')

class TestUtils_split_nodes_delimiter(unittest.TestCase):
    def test_split_nodes_delimiter_no_nodes(self):
        new_nodes = split_nodes_delimiter([], "`", TextType.CODE)
        self.assertEqual(new_nodes, [])

    def test_split_nodes_delimiter_not_text_node(self):
        node = TextNode("This is text is italic", TextType.ITALIC)
        new_nodes = split_nodes_delimiter([node], "*", TextType.CODE)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes, [
            TextNode("This is text is italic", TextType.ITALIC),
        ])

    def test_split_nodes_delimiter_no_delimiter(self):
        node = TextNode("This is text with a code block word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a code block word", TextType.TEXT),
        ])

    def test_split_nodes_delimiter_no_closing_delimiter(self):
        node = TextNode("This is text with a `code block word", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word `second code block`.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 5)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word ", TextType.TEXT),
            TextNode("second code block", TextType.CODE),
            TextNode(".", TextType.TEXT),
        ])

    def test_split_nodes_delimiter_bold(self):
        node = TextNode("**This is text** with a bold block.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 2)
        self.assertEqual(new_nodes, [
            TextNode("This is text", TextType.BOLD),
            TextNode(" with a bold block.", TextType.TEXT),
        ])

    def test_split_nodes_delimiter_italic(self):
        node = TextNode("*This is text* with an *italic block*.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes, [
            TextNode("This is text", TextType.ITALIC),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
            TextNode(".", TextType.TEXT),
        ])

class TestUtils_extract_markdown_images(unittest.TestCase):
    def test_extract_markdown_images_no_images(self):
        text = "This is text with no images."
        images = extract_markdown_images(text)
        self.assertEqual(images, [])

    def test_extract_markdown_images_only_link(self):
        text = "This is text with one link [rick roll](https://i.imgur.com/aKaOqIh.gif)."
        images = extract_markdown_images(text)
        self.assertEqual(images, [])

    def test_extract_markdown_images_one_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) image."
        images = extract_markdown_images(text)
        self.assertEqual(images, [("rick roll", "https://i.imgur.com/aKaOqIh.gif")])
    
    def test_extract_markdown_images_one_image_no_alt(self):
        text = "This is text with a ![](https://i.imgur.com/aKaOqIh.gif) image."
        images = extract_markdown_images(text)
        self.assertEqual(images, [("", "https://i.imgur.com/aKaOqIh.gif")])

class TestUtils_extract_markdown_links(unittest.TestCase):
    def test_extract_markdown_links_no_links(self):
        text = "This is text with no links."
        links = extract_markdown_links(text)
        self.assertEqual(links, [])

    def test_extract_markdown_links_with_link_and_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        links = extract_markdown_links(text)
        self.assertEqual(links, [("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_extract_markdown_links_with_link_and_image_no_alt(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and [](https://i.imgur.com/fJRm4Vk.jpeg)"
        links = extract_markdown_links(text)
        self.assertEqual(links, [("", "https://i.imgur.com/fJRm4Vk.jpeg")])

class TestUtils_split_nodes_image(unittest.TestCase):
    def test_split_nodes_image_no_images(self):
        node = TextNode("This is text with no images.", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes, [
            TextNode("This is text with no images.", TextType.TEXT),
        ])

    def test_split_nodes_image_one_image(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) image.", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" image.", TextType.TEXT),
        ])

    def test_split_nodes_image_one_link(self):
        node = TextNode("This is text with a [obi wan](https://i.imgur.com/fJRm4Vk.jpeg) link.", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a [obi wan](https://i.imgur.com/fJRm4Vk.jpeg) link.", TextType.TEXT),
        ])

class TestUtils_split_nodes_link(unittest.TestCase):
    def test_split_nodes_link_no_links(self):
        node = TextNode("This is text with no links.", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes, [
            TextNode("This is text with no links.", TextType.TEXT),
        ])

    def test_split_nodes_link_one_link(self):
        node = TextNode("This is text with a [obi wan](https://i.imgur.com/fJRm4Vk.jpeg) link.", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("obi wan", TextType.LINK, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" link.", TextType.TEXT),
        ])

    def test_split_nodes_link_one_image(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) image.", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) image.", TextType.TEXT),
        ])

class TestUtils_text_to_textnodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 10)
        self.assertEqual(nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ])

class TestUtils_markdown_to_blocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        text = '''   # This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
'''
        blocks = markdown_to_blocks(text)
        self.assertEqual(len(blocks), 3)
        print(f"blocks: {blocks}")
        self.assertEqual(blocks, [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
        ])
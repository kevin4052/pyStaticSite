import unittest

from utils import *

class TestUtils(unittest.TestCase):
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
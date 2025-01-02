import unittest

from htmlnode import HTMLNode, LeafNode

class TestHtmlNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("div", "This is a div node")
        self.assertEqual(repr(node), "HTMLNode(div, This is a div node, None, None)")

    def test_to_html(self):
        node = HTMLNode("div", "This is a div node")
        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html(self):
        node = HTMLNode("div", "This is a div node", None, {"id": "test"})
        self.assertEqual(node.props_to_html(), ' id="test"')

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph node")
        self.assertEqual(node.to_html(), "<p>This is a paragraph node</p>")

    def test_to_html_with_props(self):
        node = LeafNode("a", "This is a link node", {"href": "https://www.boot.dev"})
        self.assertEqual(node.to_html(), '<a href="https://www.boot.dev">This is a link node</a>')

    def test_to_html_no_tag(self):
        node = LeafNode(value="This is a paragraph node")
        self.assertEqual(node.to_html(), "This is a paragraph node")

    def test_to_html_no_value(self):
        node = LeafNode("p")
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_no_tag_no_value(self):
        node = LeafNode()
        self.assertRaises(ValueError, node.to_html)
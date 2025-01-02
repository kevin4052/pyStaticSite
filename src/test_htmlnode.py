import unittest

from htmlnode import HTMLNode

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

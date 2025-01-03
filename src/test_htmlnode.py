import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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
        node = LeafNode(None, "This is a paragraph node")
        self.assertEqual(node.to_html(), "This is a paragraph node")

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode("div", [LeafNode("p", "This is a paragraph node")])
        self.assertEqual(node.to_html(), "<div><p>This is a paragraph node</p></div>")

    def test_to_html_nested(self):
        node = ParentNode(
            "div",
            [
                ParentNode("div", [
                    LeafNode("h3", "Section Title", {"class": "font-semibold text-lg"}),
                    LeafNode("p", "section info"),
                ], {"class": "flex flex-col items-center justify-center"}),
            ],
            {"class": "container"}
        )
        self.assertEqual(node.to_html(), '<div class="container"><div class="flex flex-col items-center justify-center"><h3 class="font-semibold text-lg">Section Title</h3><p>section info</p></div></div>')

    def test_to_html_with_props(self):
        node = ParentNode("div", [LeafNode("p", "This is a paragraph node")], {"id": "test"})
        self.assertEqual(node.to_html(), '<div id="test"><p>This is a paragraph node</p></div>')

    def test_to_html_no_tag(self):
        node = ParentNode(children=[LeafNode("p", "This is a paragraph node")])
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_no_children(self):
        node = ParentNode("div")
        self.assertRaises(ValueError, node.to_html)
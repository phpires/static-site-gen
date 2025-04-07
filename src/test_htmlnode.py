import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        html_node = HTMLNode(tag="a", value="bootdev", props={"href": "www.boot.dev"})
        with self.assertRaises(NotImplementedError):
            html_node.to_html()
    
    def test_default_values(self):
        html_node = HTMLNode()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, None)
    
    def test_repr(self):
        html_node = HTMLNode(tag="a", value="bootdev", props={"href": "www.boot.dev"})
        expected_repr="HTMLNode(tag=a, value=bootdev, children=None, props={'href': 'www.boot.dev'})"
        self.assertEqual(str(html_node), expected_repr)

    def test_props_to_html(self):
        html_node = HTMLNode(tag="a", value="bootdev", props={"href": "www.boot.dev"})
        self.assertEqual(html_node.props_to_html(), ' href="www.boot.dev"')

    def test_values(self):
        html_node = HTMLNode(
            "div",
            "Depressed and lost perharps."
        )

        self.assertEqual(
            html_node.tag,
            "div"
        )

        self.assertEqual(
            html_node.value,
            "Depressed and lost perharps."
        )

        self.assertEqual(
            html_node.children,
            None
        )

        self.assertEqual(
            html_node.props,
            None
        )
    
    def test_leaf_to_html_p(self):
        node = LeafNode("Hello, world!", "p")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("Click me!", "a", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>'
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode("Raw text example.", None)
        self.assertEqual(node.to_html(), "Raw text example.")
    
    def test_leaf_to_html_no_value(self):
        node = LeafNode(None, None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_leaf_repr(self):
        node = LeafNode("Click me!", "a", {"href": "https://www.google.com"})
        expected_repr="LeafNode(tag=a, value=Click me!, props={'href': 'https://www.google.com'})"
        self.assertEqual(str(node), expected_repr)


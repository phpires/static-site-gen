import unittest

from htmlnode import HTMLNode

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



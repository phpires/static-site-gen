import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_to_html_with_children(self):
        child_node = LeafNode("child", "span")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("grandchild", "b")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_anchor_children_grandchildren(self):
        grandchild_node = LeafNode("Click me!", "a", {"href": "https://www.google.com"})
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><span><a href="https://www.google.com">Click me!</a></span></div>',
        )

    def test_to_html_div_with_style(self):
        grandchild_node = LeafNode("grandchild", "b")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node], {"style": "background-color:aliceblue;padding:25px;"})
        self.assertEqual(
            parent_node.to_html(),
            '<div style="background-color:aliceblue;padding:25px;"><span><b>grandchild</b></span></div>'
        )
    
    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("Bold text", "b"),
                LeafNode("Normal text", None),
                LeafNode("italic text", "i"),
                LeafNode("Normal text", None),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("Bold text", "b"),
                LeafNode("Normal text", None),
                LeafNode("italic text", "i"),
                LeafNode("Normal text", None),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

    def test_text_node_to_html_TEXT(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_text_node_to_html_BOLD(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_text_node_to_html_ITALIC(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")
    
    def test_text_node_to_html_CODE(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")
    
    def test_text_node_to_html_LINK(self):
        node = TextNode("This is a text node", TextType.LINK, "www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props, {"href":"www.google.com"})

    def test_text_node_to_html_IMAGE(self):
        node = TextNode("This is a image description node", TextType.IMAGE, "www.image.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src":"www.image.com", "alt": "This is a image description node"})



import unittest
from textnode import TextNode, TextType
from inlinenode_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

class TestInlineNodeMarkdown(unittest.TestCase):
    def test_delimeter_code_code_block(self):
        old_node = TextNode("This is text with a `code block` word", TextType.TEXT)
        delimeter = "`"
        text_type = TextType.CODE

        new_nodes = split_nodes_delimiter([old_node], delimeter, text_type)

        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes
        )
    
    def test_delimeter_multiple_code_block(self):
        old_node = TextNode("This is text with a `code block` and another `code block` word", TextType.TEXT)
        delimeter = "`"
        text_type = TextType.CODE

        new_nodes = split_nodes_delimiter([old_node], delimeter, text_type)

        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and another ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT)
            ],
            new_nodes
        )
    
    def test_delimeter_code_block_on_begining(self):
        old_node = TextNode("`code block` is this right?", TextType.TEXT)
        delimeter = "`"
        text_type = TextType.CODE

        new_nodes = split_nodes_delimiter([old_node], delimeter, text_type)

        self.assertListEqual(
            [
                TextNode("code block", TextType.CODE),
                TextNode(" is this right?", TextType.TEXT)
            ],
            new_nodes
        )
    
    def test_delimeter_code_block_on_ending(self):
        old_node = TextNode("Can you check this code for me? `code block`", TextType.TEXT)
        delimeter = "`"
        text_type = TextType.CODE

        new_nodes = split_nodes_delimiter([old_node], delimeter, text_type)

        self.assertListEqual(
            [
                TextNode("Can you check this code for me? ", TextType.TEXT),
                TextNode("code block", TextType.CODE)
            ],
            new_nodes
        )
    
    def test_delimeter_bold_text(self):
        old_node = TextNode("A simple **bold text**", TextType.TEXT)
        delimeter = "**"
        text_type = TextType.BOLD

        new_nodes = split_nodes_delimiter([old_node], delimeter, text_type)

        self.assertListEqual(
            [
                TextNode("A simple ", TextType.TEXT),
                TextNode("bold text", TextType.BOLD)
            ],
            new_nodes
        )
    
    def test_delimeter_bold_text_multiple_nodes(self):
        old_nodes = []
        old_nodes.append(TextNode("A simple **bold text**. ", TextType.TEXT))
        old_nodes.append(TextNode("Another simple **bold text**.", TextType.TEXT))

        delimeter = "**"
        text_type = TextType.BOLD

        new_nodes = split_nodes_delimiter(old_nodes, delimeter, text_type)

        self.assertListEqual(
            [
                TextNode("A simple ", TextType.TEXT),
                TextNode("bold text", TextType.BOLD),
                TextNode(". ", TextType.TEXT),
                TextNode("Another simple ", TextType.TEXT),
                TextNode("bold text", TextType.BOLD),
                TextNode(".", TextType.TEXT)
            ],
            new_nodes
        )

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_multiple_images(self):
        matches = extract_markdown_images(
            text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        self.assertListEqual([
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
            ], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)
    
    def test_extract_multiple_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)


import unittest
from textnode import TextNode, TextType
from delimetersplitter import split_nodes_delimiter

class TestDelimeterSplitter(unittest.TestCase):
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


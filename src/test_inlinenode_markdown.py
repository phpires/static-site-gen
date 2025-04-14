import unittest
from textnode import TextNode, TextType
from inlinenode_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link

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
    
    def test_split_image(self):
        node = TextNode("This is an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
            ],
            new_nodes,
        )
    def test_split_single_image(self):
        node = TextNode("![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
            ],
            new_nodes,
        )
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()

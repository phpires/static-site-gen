import unittest
from block_markdown import *

class TestBlockMarkdown(unittest.TestCase):

    def test_markdown_to_blocks_simple_markdown(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_empty_lines(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line






- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_block_to_block_type_ordered_list(self):
            block="""This is a simples paragraph"""
            block_type = block_to_block_type(block)
            self.assertEqual(block_type, BlockType.PARAGRAPH)
    
    def test_block_to_block_type_heading(self):
        block_type = []

        block = "# Heading"
        block_type.append(block_to_block_type(block))

        block = "## Heading"
        block_type.append(block_to_block_type(block))

        block = "### Heading"
        block_type.append(block_to_block_type(block))

        block = "#### Heading"
        block_type.append(block_to_block_type(block))

        block = "##### Heading"
        block_type.append(block_to_block_type(block))

        block = "###### Heading"
        block_type.append(block_to_block_type(block))

        self.assertListEqual(
            block_type,
            [
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.HEADING, 
                BlockType.HEADING, 
                BlockType.HEADING
            ]
        )

    def test_block_to_block_type_code(self):
        block = """```
code
```"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)
    
    def test_block_to_block_type_quote(self):
        block="""> A quote"""

        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)
    
    def test_block_to_block_type_unordered_list(self):
        block="""- a item
- another item
- last item"""

        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)
    
    def test_block_to_block_type_ordered_list(self):
        block="""1. first item
2. second item
3. third item"""

        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_block_to_block_type_ordered_list_index_not_incremented(self):
        block="""1. first item
2. second item
5. third item"""

        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
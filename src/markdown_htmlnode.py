from block_markdown import *
from htmlnode import LeafNode, ParentNode
from inlinenode_markdown import text_to_textnodes
from textnode import text_node_to_html_node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        html_nodes.append(block_to_html_node(block))
    return ParentNode("div", html_nodes)

def get_inline_nodes(block):
    splitted_block = block.split(" ", maxsplit=1)
    return list(map(text_node_to_html_node, text_to_textnodes(splitted_block[1])))

def get_inline_nodes_multiline(block, html_tag):
    inline_nodes = []
    for element in block.splitlines():
        inline_nodes.append(ParentNode(html_tag, get_inline_nodes(element)))
    return inline_nodes

def convert_from_code(block):
    if not block.startswith("```") and not block.endswith("```"):
        raise Exception("Malformed code block")
    leaf_node = LeafNode(block.strip("```"), "code")
    return ParentNode("pre", [leaf_node])

def convert_from_heading(block):
    if not block.startswith("#"):
        raise Exception("Malformed headingblock")
    header_level = block.split(" ", maxsplit=1)[0].count("#")
    return ParentNode(f"h{header_level}", get_inline_nodes(block))

def convert_from_blockquote(block):
    new_blocks = []
    for line in block.splitlines():
        if not line.startswith(">"):
            raise Exception("Malformed quote block")
        new_blocks.append(line.strip(">"))
    return ParentNode("blockquote", get_inline_nodes("".join(new_blocks)))

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.CODE:
        return convert_from_code(block)
    elif block_type == BlockType.HEADING:
        return convert_from_heading(block)
    elif block_type == BlockType.QUOTE:
        return convert_from_blockquote(block)
    elif block_type == BlockType.UNORDERED_LIST:
        return ParentNode("ul", get_inline_nodes_multiline(block, "li"))
    elif block_type == BlockType.ORDERED_LIST:
        return ParentNode("ol", get_inline_nodes_multiline(block, "li"))
    elif block_type == BlockType.PARAGRAPH:
        inline_nodes = list(map(text_node_to_html_node, text_to_textnodes(block)))
        if len(inline_nodes) == 0:
            return LeafNode(block, "p")
        return ParentNode("p", inline_nodes)
    raise Exception("Invalid block type")

md = """>a multiline
>>blockquote"""

#print(markdown_to_html_node(md).to_html())
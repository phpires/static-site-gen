from block_markdown import *
from htmlnode import LeafNode, ParentNode, HTMLTagType

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        html_node = block_to_html_node(block)
    return html_node.to_html()

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.CODE:
        leaf_node = LeafNode(block.strip("```"), "code") #Code não tem filho!
        parent_node = ParentNode("pre", [leaf_node])
        return parent_node

block = """```
This is text that _should_ remain
the **same** even with inline stuff
```"""
print(markdown_to_html_node(block))
"""
1 - Quebrar o markdown em blocks
2 - Encontrar os inlines dentro desses blocks
    2.1 - Transformar em HTML (LeafNode?)
3 - Adicionar os leafnodes gerados no ParentNode, que vai ser o block com os inlines dentro dele.
4 - Um block dentro de um block?

"""
    
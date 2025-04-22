from block_markdown import markdown_to_blocks, block_to_block_type, BlockType

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING and block[1] != "#":
            return block.lstrip("#").strip()
    raise Exception("Not a h1 header.")

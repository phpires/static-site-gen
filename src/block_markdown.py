from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = " ",
    HEADING = r"^(#{1,6})\s+(.+)$", #OK
    CODE = r'^```(?:\w+)?\s*\n(.*?)(?=^```)```', #ok
    QUOTE = r"^>\s*(.+)$", #ok
    UNORDERED_LIST = r"^\s*[-+*]\s+(.+)$",
    ORDERED_LIST = r"^\s*\d+\.\s+(.+)$"


def markdown_to_blocks(markdown):
    splitted_blocks = markdown.split("\n\n")
    stripped_blocks = list(map(lambda s : s.strip(), splitted_blocks))
    return list(filter(lambda s : s != "", stripped_blocks))

def block_to_block_type(block):
    for block_type in BlockType:
        if block_type == BlockType.PARAGRAPH:
            continue
        pattern = block_type.value[0]
        
        if re.findall(pattern, block, re.DOTALL | re.MULTILINE):
            if block_type == BlockType.ORDERED_LIST:
                lines = block.splitlines()
                line_counter = 1
                for line in lines:
                    if (str(line_counter) != line[0]):
                        return BlockType.PARAGRAPH
                    line_counter += 1
                return block_type
            return block_type
    return BlockType.PARAGRAPH

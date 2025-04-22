import os

from block_markdown import markdown_to_blocks, block_to_block_type, BlockType
from markdown_htmlnode import markdown_to_html_node

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING and block[1] != "#":
            return block.lstrip("#").strip()
    raise Exception("Not a h1 header.")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as md_file:
        md_content = md_file.read()
        print(f"Opening md file: {md_file.name}")
    
    with open(template_path) as template_html_file:
        template_html_content = template_html_file.read()
        print(f"Opening md file: {template_html_file.name}")
    
    html_content = markdown_to_html_node(md_content).to_html()
    h1_title = extract_title(md_content)
    page_html = template_html_content.replace("{{ Title }}", h1_title).replace("{{ Content }}", html_content)
    
    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    
    with open(dest_path, 'w') as f:
        f.write(page_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    content_dir = os.listdir(dir_path_content)
    print(f"Listing content on {content_dir}")
    for content in content_dir:
        content_path = os.path.join(dir_path_content, content)
        if os.path.isfile(content_path):
            generate_page(content_path, template_path, dest_dir_path)
        else:
            generate_pages_recursive(content_path, template_path, dest_dir_path)
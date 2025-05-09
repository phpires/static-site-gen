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

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as md_file:
        md_content = md_file.read()
        print(f"Opening md file: {md_file.name}")
    
    with open(template_path) as template_html_file:
        template_html_content = template_html_file.read()
        print(f"Opening html template: {template_html_file.name}")
    
    html_content = markdown_to_html_node(md_content).to_html()
    h1_title = extract_title(md_content)
    page_html = template_html_content.replace("{{ Title }}", h1_title).replace("{{ Content }}", html_content)
    page_html = page_html.replace("href=\"/", f"href=\"{basepath}").replace("src=\"/", f"src=\"{basepath}")
    
    if not os.path.exists(os.path.dirname(dest_path)):
        print(f"Destiny path not found. Creating: {dest_path}")
        os.makedirs(os.path.dirname(dest_path))
    
    with open(dest_path, 'w') as f:
        print(f"Creating html to {dest_path}")
        f.write(page_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    content_dir = os.listdir(dir_path_content)
    print(f"Listing content on {dir_path_content}: {content_dir}")
    for content in content_dir:
        content_path = os.path.join(dir_path_content, content)
        print(f"Analyzing content on {content_path}")
        if os.path.isfile(content_path):
            generate_page(content_path, template_path, os.path.join(dest_dir_path, "index.html"), basepath)
        else:
            new_dest_dir_path = os.path.join(dest_dir_path, content)
            generate_pages_recursive(content_path, template_path, new_dest_dir_path, basepath)
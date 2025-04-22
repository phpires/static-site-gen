from textnode import TextNode, TextType
from copy_static import copy_from_static_to_public
from generate_page import generate_pages_recursive

import os
import shutil

public_path = "./public"
static_path = "./static"

content_index_md_path = "./content"
template_html_path = "./template.html"
public_index_html_path = "./public"

def main():
    print("Deleting public dir")
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
    copy_from_static_to_public(static_path, public_path)
    generate_pages_recursive(content_index_md_path, template_html_path, public_index_html_path)

main()
from textnode import TextNode, TextType
from copy_static import copy_from_static_to_public
from generate_page import generate_pages_recursive

import os
import shutil
import sys 

static_path = "./static"
content_path = "./content"
template_html_path = "./template.html"
doc_path = "./docs"

def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    print("Deleting doc dir")
    if os.path.exists(doc_path):
        shutil.rmtree(doc_path)
    copy_from_static_to_public(static_path, doc_path)
    generate_pages_recursive(content_path, template_html_path, doc_path, basepath)

main()
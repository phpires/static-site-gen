from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimeter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        splitted_nodes = old_node.text.split(delimeter)
        if len(splitted_nodes) % 2 == 0:
            raise Exception("Malformed markdown. Section open?")
        for i in range(0, len(splitted_nodes)):
            #Text type is on odd index.
            if i % 2 == 0 and splitted_nodes[i] != "":
                new_nodes.append(TextNode(splitted_nodes[i], TextType.TEXT))
            elif i % 2 != 0:
                new_nodes.append(TextNode(splitted_nodes[i], text_type))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        old_node_txt = old_node.text
        imgs_md = extract_markdown_images(old_node_txt)
        if len(imgs_md) == 0:
            new_nodes.append(old_node)
            continue
        for img_md in imgs_md:
            alt_text, img_link = img_md
            splitted_txt = old_node_txt.split(f"![{alt_text}]({img_link})", 1)
            if len(splitted_txt) % 2 != 0:
                raise Exception("Malformed image markdown")
            if splitted_txt[0] != '':
                new_nodes.append(TextNode(splitted_txt[0], TextType.TEXT))
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, img_link))
            old_node_txt = splitted_txt[1]
        if old_node_txt != '':
            new_nodes.append(TextNode(old_node_txt, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        old_node_txt = old_node.text
        links_md = extract_markdown_links(old_node_txt)
        if len(links_md) == 0:
            new_nodes.append(old_node)
            continue
        for link_md in links_md:
            link_text, link_url = link_md
            splitted_txt = old_node_txt.split(f"[{link_text}]({link_url})", 1)
            if len(splitted_txt) % 2 != 0:
                raise Exception("Malformed link markdown")
            if splitted_txt[0] != '':
                new_nodes.append(TextNode(splitted_txt[0], TextType.TEXT))
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            old_node_txt = splitted_txt[1]
        if old_node_txt != '':
            new_nodes.append(TextNode(old_node_txt, TextType.TEXT))
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

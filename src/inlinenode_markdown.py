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
        images_markdown = extract_markdown_images(old_node_txt)
        if len(images_markdown) == 0:
            raise Exception("Not a image markdown section")
        def create_new_nodes(images_markdown, old_node_txt):
            nonlocal new_nodes
            if len(images_markdown) == 0:
                return
            image_alt, image_link = images_markdown[0]
            splitted_markdown = old_node_txt.split(f"![{image_alt}]({image_link})")
            print(splitted_markdown)
            if splitted_markdown[0] == "" and splitted_markdown[1] != "":
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
                new_nodes.append(TextNode(splitted_markdown[1], TextType.TEXT))
            elif splitted_markdown[0] == "" and splitted_markdown[1] == "":#single img case
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            else:
                new_nodes.append(TextNode(splitted_markdown[0], TextType.TEXT))
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            
            return create_new_nodes(images_markdown[1:], splitted_markdown[1])
    create_new_nodes(images_markdown, old_node_txt)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        old_node_txt = old_node.text
        links_markdown = extract_markdown_links(old_node_txt)
        if len(links_markdown) == 0:
            raise Exception("Not a link markdown section")
        def create_new_nodes(links_markdown, old_node_txt):
            nonlocal new_nodes
            if len(links_markdown) == 0:
                return
            link_text, link_url = links_markdown[0]
            splitted_markdown = old_node_txt.split(f"[{link_text}]({link_url})")
            if splitted_markdown[0] == "" and splitted_markdown[1] != "":
                new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
                new_nodes.append(TextNode(splitted_markdown[1], TextType.TEXT))
            elif splitted_markdown[0] == "" and splitted_markdown[1] == "":
                new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            else:
                new_nodes.append(TextNode(splitted_markdown[0], TextType.TEXT))
                new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            
            return create_new_nodes(links_markdown[1:], splitted_markdown[1])
    create_new_nodes(links_markdown, old_node_txt)
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

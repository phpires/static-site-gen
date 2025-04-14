from textnode import TextNode, TextType

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

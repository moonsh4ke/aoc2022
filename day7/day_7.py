from treelib import Node, Tree
from collections import namedtuple

def is_command(line: list) -> bool:
    return line[0] == "$"

def get_size(node: Node) -> int:
    print(node)
    if(node.data.type == "f"):
        return node.data.size

    # obtener los hijos en una lista
    childrens = tree.children(node.identifier)

    # node is a directory
    size = 0
    for child in childrens:
        size += get_size(child)
    node.data = FNode(node.data.type, size)
    return size

# a node is either a file or directory (type = "f" | "d")
FNode = namedtuple("FNode", ['type', 'size'])

tree = Tree()

root = tree.create_node(tag="/", data=FNode("d", 0))
current_node = root

with open("test.txt", "r") as f:
    while(True):
        line = f.readline()
        if(line == ''):
            break
        line = line.split()
        if(is_command(line) == True):
            _, cmd, *arg = tuple(line)
            if(cmd == "cd"):
                arg = arg[0]
                if(arg == ".."):
                    current_node = tree.parent(current_node.identifier)
                    print("current node now is ", current_node)
                else:
                    childrens = tree.children(current_node.identifier)
                    for child in childrens:
                        if child.tag == arg:
                            current_node = child
                            break
                    print("current node now is ", current_node)
        else:
            node_name = line[1]
            if(line[0] == "dir"):
                print("created node", node_name)
                tree.create_node(tag=node_name,
                parent=current_node, data=FNode("d", 0))
            else:
                file_size = line[0]
                print("created node", node_name)
                tree.create_node(tag=node_name,
                parent=current_node, data=FNode("f", int(file_size)))

# tree.show()
# tree.show(data_property="size")

get_size(root)

# total = 0
# for n in tree.nodes.values():
#     if n.data.type == "d" and n.data.size <= 100000:
#         total += n.data.size

used = root.data.size
unused = 70000000 - used
need = 30000000 - unused

options = list()
for n in tree.nodes.values():
    if n.data.type == "d" and n.data.size >= need:
        options.append(n.data.size)

print(min(options))

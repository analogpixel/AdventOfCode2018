#!/usr/bin/env python

from treelib import Node, Tree

# https://treelib.readthedocs.io/en/latest/examples.html#advanced-usage

def walkTree(tree, rootNode, path):
    
    d = list(map(lambda x: x.tag, tree.children(rootNode)))
    d.sort()

    for z in d:
        path = walkTree(tree, z, path + z)
    
    return path


input = list(map( lambda x: x.strip(), open("test_input.txt").readlines() ))
tree = Tree()
tree.create_node("root","root")

# first figure out how many steps there are and then sort them
# by their name
for lines in input:
    (l1, l2) = (lines[5], lines[36])
    print(lines)
    if tree.contains(l1) and tree.contains(l2):
        tree.move_node(l2, l1 )
    elif tree.contains(l1) and not tree.contains(l2):
        tree.create_node(l2,l2, parent=l1)
    elif not tree.contains(l1) and tree.contains(l2):
        # get the root for l2 and make that the root for l1
        # then move l2 under l1
        tree.create_node(l1,l1, parent= tree.parent(l2) )
        tree.move_node(l2,l1)
        
    else:
        tree.create_node(l1,l1, parent="root")
        tree.create_node(l2,l2, parent=l1)

tree.show()
print( walkTree(tree, 'root', '') )
import random
from BinarySearchTree import BinarySearchTree
random.seed(77)

def example_tree(size=42):
    values = [61,89,66,43,51,16,55,11,79,77,82,32]
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree

def extended_tree(size=42):
    values = [61,89,66,43,51,16,55,11,79,77,82,32,100,90]
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree

def random_tree(size=42):
    values = random.sample(range(1,1000),42)
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree



bst = BinarySearchTree()
# for v in values:
#     bst.insert(v)

# bst.inOrder()
# print("")

# items = [ 1,3,981, 510, 1000]

# for item in items:
#     r = bst.search(item)
#     if r is None:
#         print(item, " não encontrado")
#     else:
#         print(r.root.data, " encontrado")

bst = extended_tree()
bst.inOrder()

print("\n ----------")
print("Maxime:", bst.findMax())
print("Minimum:", bst.findMin())

print("\n ----------")
value = 61 
bst.removeNode(value)
print("After removing {}".format(value))
bst.inOrder()

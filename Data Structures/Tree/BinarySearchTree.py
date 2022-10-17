from BinaryTree import BinaryTree
from node import Node

ROOT = "root"

class BinarySearchTree(BinaryTree):
    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value < x. data:
                x = x.left 
            else:
                x = x.right

        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    def search(self, value, node=0):
        if node == 0:
            node = self.root
        if node is None:
            return node
        if node.data == value:
            return BinarySearchTree(node)
        if value < node.data:
            return self.search(value, node.left)
        return self.search(value, node.right)

    def inOrder(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.inOrder(node.left)
        print(node,end=" ")
        if node.right:
            self.inOrder(node.right)
        
    def findMax(self, node=ROOT):
        if node == ROOT :
            node = self.root
        while node.right:
            node = node.right
        return node.data


    def findMin(self, node = ROOT):
        if node == ROOT :
            node = self.root
        while node.left:
            node = node.left
        return node.data

    def removeNode(self,value, node=ROOT):
        if node == ROOT:
            node = self.root
        if node is None:
            return node
        if value < node.data:
            node.left = self.removeNode(value, node.left)
        elif value > node.data:
            node.right = self.removeNode(value,node.right)
        else: 
            if node.left is None and node.right is None:
                return None
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                replaceNode = self.findMin(node.right)
                node.data = replaceNode
                node.right = self.removeNode(replaceNode,node.right)
        
        return node
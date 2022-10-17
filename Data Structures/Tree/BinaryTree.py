from node import Node

class BinaryTree:

    def __init__(self, data=None, node = None):
        if node:
            self.root = node
        if data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            print("(", end="")
            self.simetric_traversal(node.left)
        print(node,end="")
        if node.right:
            self.simetric_traversal(node.right)
            print(")", end="")

    def inOrder(self,node=None):
       pass

    def preOrder(self,node=None):
        pass


    def posOrder(self,node=None): # I need to loook your children first 
        if node is None:
            node = self.root
        if node.left:
            self.posOrder(node.left)
        if node.right:
            self.posOrder(node.right)
        print(node)

    def height(self, node = None):
        hleft = 0 
        hright = 0
        if node is None:
            node = self.root
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        
        if hright> hleft:
            return hright+1
        else :
            return hleft+1
        

    

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
        else:
            current = self.root
            while True:
                last = current
                if value <= current.left:
                    current = current.left
                    if current == None:
                        last.left = new_node
                        return
                else:
                    current = current.right
                    if current == None:
                        last.right = new_node
                        return 


    
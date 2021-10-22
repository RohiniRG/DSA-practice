''' structure of tree node:

class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
        self.height=1

'''

class Solution:
    def insertToAVL(self, root, key):
        # add key to AVL (if it is not present already)
        # return root node
        if not root:
            root = Node(key)
            return root
        
        elif key > root.data:
            root.right = self.insertToAVL(root.right, key)
        elif key < root.data:
            root.left = self.insertToAVL(root.left, key)
        
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        bal = self.getBalance(root)

        if bal > 1 and key > root.left.data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        if bal > 1 and key < root.left.data:
            return self.rightRotate(root)
            
        if bal < -1 and key > root.right.data:
            return self.leftRotate(root)

        if bal < -1 and key < root.right.data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return root
         
    def getHeight(self, root):
        if not root:
            return 0
        return root.height
        
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
        
        
    def rightRotate(self, rt):
        child = rt.left
        g_child = child.right
        
        child.right = rt
        rt.left = g_child
        
        rt.height = 1 + max(self.getHeight(rt.left), self.getHeight(rt.right))
        child.height = 1 + max(self.getHeight(child.left), self.getHeight(child.right))
            
        return child
        
    def leftRotate(self, rt):
        child = rt.right
        g_child = child.left
        
        child.left = rt
        rt.right = g_child
        
        rt.height = 1 + max(self.getHeight(rt.left), self.getHeight(rt.right))
        child.height = 1 + max(self.getHeight(child.left), self.getHeight(child.right))
            
        return child
      

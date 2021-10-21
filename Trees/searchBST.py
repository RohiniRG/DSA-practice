class Node:
    def _init_(self, key):
        self.left = None
        self.right = None
        self.data = key


def inorder(temp):
    if not temp:
        return
    # LVR
    inorder(temp.left)
    print(temp.data)
    inorder(temp.right)


def search(self, node, x):
    if not node:
        return 0
    
    if node.data == x:
        return 1
    
    if node.data < x:
        return self.search(node.right, x)
    else:
        return self.search(node.left, x)


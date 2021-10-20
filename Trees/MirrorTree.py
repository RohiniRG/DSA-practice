class Node:
    def __init__(self, key):
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


def mirror(rootnode):
    if not rootnode:
        return

    q = []
    q.append(rootnode)

    while len(q):
        root = q.pop(0)
        if root.left and root.right:
            temp = root.left
            root.left = root.right
            root.right = temp
            q.append(root.left)
            q.append(root.right)
        elif root.left:
            root.right = root.left
            root.left = None
            q.append(root.right)

        elif root.right:
            root.left = root.right
            root.right = None
            q.append(root.left)

    return rootnode


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.left.right = Node(12)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)
    print("Original Tree:")
    inorder(root)
    root = mirror(root)
    print()
    print("Mirrored Tree:")
    inorder(root)
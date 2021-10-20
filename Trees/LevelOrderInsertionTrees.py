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


def LevelOrderInsertion(temp, key):
    if not temp:
        root = Node(key)
        return root

    q = []
    q.append(temp)

    while len(q) > 0:
        start = q.pop(0)

        if not start.left:
            start.left = Node(key)
            break
        else:
            q.append(start.left)

        if not start.right:
            start.right = Node(key)
            break
        else:
            q.append(start.right)


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)

    print("Inorder traversal before insertion:", end=" ")
    inorder(root)

    key = 12
    LevelOrderInsertion(root, key)

    print()
    print("Inorder traversal after insertion:", end=" ")
    inorder(root)

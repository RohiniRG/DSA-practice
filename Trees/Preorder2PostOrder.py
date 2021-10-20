class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key


def postorder(temp):
    if not temp:
        return
    postorder(temp.left)
    postorder(temp.right)
    print(temp.data)


def pre2post(pre, size):
    root = Node(pre[0])

    stack = []
    stack.append(root)

    temp = root
    for node in pre[1:]:
        if node < stack[-1].data:
            temp.left = Node(node)
            stack.append(temp.left)
            temp = temp.left

        elif node > stack[-1].data:
            while len(stack) and node > stack[-1].data:
                temp = stack.pop()

            temp.right = Node(node)
            stack.append(temp.right)
            temp = temp.right

    return root


if __name__ == "__main__":
    N = 5
    arr = [40, 30, 35, 80, 100]
    root = pre2post(arr, N)
    print("Postorder: ")
    postorder(root)

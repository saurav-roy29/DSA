class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def right_side_traversal(root):
    if root is None:
        return None
    
    q = []
    q.append(root)
    answer = []

    while q:
        count = len(q)

        while count > 0:
            num = q.pop(0)
            answer.append(num.data)

            if num.right:
                q.append(num.right)

            count-=1
    return answer


def print_node(root):
    if root == None:
        return None
    
    print(root.data, end=" ")
    print_node(root.left)
    print_node(root.right)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print(right_side_traversal(root))
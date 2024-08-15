class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def level_order_traversal(root):
    if root == None:
        return None

    q = []
    q.append(root)
    answer = []

    while q:
        count = len(q)
        ls = []
        while count > 0:
            temp = q.pop()
            ls.append(temp.data)

            if temp.left:
                q.append(temp.left)
            
            if temp.right:
                q.append(temp.right)
            
            count-=1

        answer.append(ls)
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

    print(level_order_traversal(root))
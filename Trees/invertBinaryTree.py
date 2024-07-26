class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printTree(root):
    if root == None:
        return
    
    print(root.data, end=" ")
    printTree(root.left)
    printTree(root.right)


def invertTree(root):
    if root == None:
        return
    
    root.left, root.right = root.right, root.left

    invertTree(root.left)
    invertTree(root.right)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    printTree(root)
    print()
    invertTree(root)
    printTree(root)


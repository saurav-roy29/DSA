class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isSameTree(rootA, rootB):

    if rootA is None and rootB is None:
        return True
    elif rootA and rootB:
        # if both root exist
        return (rootA.data == rootB.data and isSameTree(rootA.left, rootB.left) and isSameTree(rootA.right, rootB.right))
    else:
        # if any of the root is empty
        return False
    
def printTree(root):
    if root == None:
        return
    
    print(root.data, end=" ")
    printTree(root.left)
    printTree(root.right)


if __name__ == "__main__":
    rootA = TreeNode(1)
    rootA.left = TreeNode(2)
    rootA.right = TreeNode(3)

    rootB = TreeNode(1)
    rootB.left = TreeNode(2)
    rootB.right = TreeNode(3)


    print(isSameTree(rootA, rootB))



        
# are the 2 tree similar
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    

def isSameTree(root1, root2):
    
    if root1 == None and root2 == None:
        return True
    
    if root1 and root2:
        if root1.data == root2.data and isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right):
            return True
        else:
            return False
    

if __name__ == "__main__":
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)

    print(isSameTree(root1, root2))
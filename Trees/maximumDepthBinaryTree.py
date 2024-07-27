# To find the maximum depth of a Binary Tree
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def max_depth_tree(root):
    if root == None:
        return 0
    
    l_depth = max_depth_tree(root.left)
    r_depth = max_depth_tree(root.right)

    return max(l_depth+1, r_depth+1)

def print_tree(root):
    if root == None:
        return
    
    print(root.data, end=" ")
    print_tree(root.left)
    print_tree(root.right)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print(max_depth_tree(root))
        
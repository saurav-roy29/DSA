# Find the diameter of a Binary Tree
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if root == None:
        return 0
    
    left_height = height(root.left)
    right_height = height(root.right)

    return max(left_height, right_height) + 1

def diameter(root):
    if root == None:
        return 0

    # Find max diameter from left wing
    left_diameter = diameter(root.left)

    # Find max diameter from right wing
    right_diameter = diameter(root.right)

    # Find max diameter after passing from the root
    left_height = height(root.left)
    right_height = height(root.right)
    central_diameter = left_height + right_height

    return max(left_diameter, max(central_diameter, right_diameter))        
    
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

    print(diameter(root))
        
# To check if the tree is balanced or not

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right =  None

def height_bt(root):

    if root == None:
        return 0 
    
    left_height = height_bt(root.left)
    right_height = height_bt(root.right)

    return max(left_height, right_height) + 1


def is_balanced_tree(root):
    if root == None:
        return True
    
    left_height_node = height_bt(root.left)
    right_height_node = height_bt(root.right)

    if abs(left_height_node - right_height_node) > 1:
        return False
    
    
    if is_balanced_tree(root.left) and is_balanced_tree(root.right):
        return True
    else:
        return False

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    
    print(is_balanced_tree(root))
        
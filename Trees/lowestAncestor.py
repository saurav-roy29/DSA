# To return the lowest ancestor value of a binary search tree (BST)
from typing import Optional

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right =  None

def lowest_ancestor_bt(root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode])-> TreeNode:
    
    # Since this is a BST we will take into consideration it's format
    if root == None:
        return None
    

    if (root.data < p.data) and (root.data < q.data):
        return lowest_ancestor_bt(root.right, p, q)

    if (root.data > p.data) and (root.data > q.data):
        return lowest_ancestor_bt(root.left, p, q)
    
    return root

if __name__ == "__main__":

    # BST
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    p = TreeNode(2)
    q = TreeNode(3)

    answer = lowest_ancestor_bt(root, p, q)
    print(answer.data)
        
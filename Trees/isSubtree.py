# To check if the tree is a subtree of a tree
from typing import Optional

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right =  None


def are_nodes_similar(parent: Optional[TreeNode], child: Optional[TreeNode])->bool:
    if parent is None and child is None:
        return True
    
    if parent is None or child is None:
        return False
    
    return (parent.data == child.data and are_nodes_similar(parent.left,child.left ) and are_nodes_similar(parent.right, child.right))

def is_subtree(parent: Optional[TreeNode], child: Optional[TreeNode])->bool:
    
    if parent is None:
        return False
    
    if child is None:
        return True
    
    if are_nodes_similar(parent, child):
        return True
    
    return is_subtree(parent.left, child) or is_subtree(parent.right, child)

if __name__ == "__main__":
    rootA = TreeNode(1)
    rootA.left = TreeNode(2)
    rootA.right = TreeNode(3)
    
    rootB = TreeNode(1)
    rootB.left = TreeNode(2)
    rootB.right = TreeNode(3)

    print(is_subtree(rootA, rootB))
        
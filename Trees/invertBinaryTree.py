class Node:
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

def mirrorTree(root):
    if root == None:
        return None
    
    if root.left and root.right:
        temp = root.left
        root.left = root.right
        root.right = temp

    root.left = mirrorTree(root.left)
    root.right = mirrorTree(root.right)


if __name__  == "__main__":
    root = Node(8)
    root.left = Node(1)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)

    newroot = mirrorTree(root)
    printTree(newroot)    


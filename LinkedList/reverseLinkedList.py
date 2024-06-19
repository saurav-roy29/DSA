class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert():

    ls = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for obj in ls:
        if obj == -1:
            break
        else:
            newnode = Node(obj)
            if head is not None:
                tail.next = newnode
                tail = newnode
            else:
                head = newnode
                tail = newnode

    return head


def reverseNode(head):
    if head == None:
        return None
    
    prevptr = None
    currptr = head
    nextptr = None

    while currptr is not None:
        nextptr = currptr.next
        currptr.next = prevptr

        prevptr = currptr
        currptr = nextptr
    
    return prevptr

def printNode(head):
    if head == None:
        return
    
    temp = head
    while temp is not None:
        print(temp.data, end= " ")
        temp = temp.next


if __name__ == "__main__":
    head = insert()
    printNode(head)
    newHead = reverseNode(head)
    print()
    printNode(newHead)




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
            newNode = Node(obj)
            if head == None:
                head = newNode
                tail = newNode
            else:
                tail.next = newNode
                tail = newNode

    return head

def Print(head):
    if head == None:
        return

    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next


def removeNNode(head, n):
    if head == None:
        return None
    
    start = Node(-1)
    start.next = head

    fastptr = start
    slowptr = start
    
    for i in range(1, n+1):
        fastptr = fastptr.next

    while fastptr.next is not None:
        slowptr = slowptr.next
        fastptr = fastptr.next

    slowptr.next = slowptr.next.next
    return start.next

head = insert()
Print(head)
print()
newhead = removeNNode(head, 2)
Print(newhead)

        

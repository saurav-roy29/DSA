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
            if head is None:
                head = newNode
                tail = newNode
            else:
                tail.next = newNode
                tail = newNode
    return head

def Print(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next


def reorder(head):
    if head == None:
        return
    
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    
    # reverse second half of the list
    second = slow.next
    prev = slow.next = None

    while second:
        temp = second.next
        second.next = prev
        prev = second
        second = temp

    # merge 2 halves
    
    first, second = head, prev
    while second:
        temp1 = first.next
        temp2 = second.next

        first.next = second
        second.next  = temp1

        first = temp1
        second = temp2


head = insert()
Print(head)
print()
reorder(head)
Print(head)

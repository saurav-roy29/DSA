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
        print(temp.data, end= " ")
        temp = temp.next


def mergeLL(head1, head2):
    
    if head1 == None and head2 == None:
        return None
    
    if head1 == None:
        return head2
    
    if head2 == None:
        return head1
    
    temp1 = head1
    temp2 = head2
    answer = Node(-1)
    tail = answer

    while (temp1 is not None) and (temp2 is not None):
        if temp1.data <= temp2.data:
            newNode = Node(temp1.data)
            tail.next = newNode
            temp1 = temp1.next
            tail = tail.next
        else:
            newNode = Node(temp2.data)
            tail.next = newNode
            temp2 = temp2.next
            tail = tail.next

    while temp1 is not None:
        newNode = Node(temp1.data)
        tail.next = newNode
        temp1 = temp1.next
        tail = tail.next
    
    while temp2 is not None:
        newNode = Node(temp2.data)
        tail.next = newNode
        temp2 = temp2.next
        tail = tail.next

    return answer.next

head1 = insert()
head2 = insert()
Print(head1)
print()
Print(head2)
print()
newHead = mergeLL(head1, head2)
Print(newHead)
        

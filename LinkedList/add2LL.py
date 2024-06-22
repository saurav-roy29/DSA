# add LL
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

def printNode(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next

def add2Numbers(l1, l2):
    dummy = Node(-1)
    cur = dummy

    carry = 0
    while l1 or l2 or carry:
        v1 = l1.data if l1 else 0
        v2 = l2.data if l2 else 0

        # new digit
        val = v1 + v2 + carry
        carry = val // 10
        val = val%10
        cur.next = Node(val)

        # update ptrs
        cur = cur.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next

if __name__ == "__main__":
    head1 = insert()
    head2 = insert()
    newhead = add2Numbers(head1, head2)
    printNode(newhead)




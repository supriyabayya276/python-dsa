 class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def addafter(head, d, s):
    temp = head

    while temp is not None:
        if s == temp.data:
            break
        temp = temp.next

    if temp is None:
        print("specific Node not found")
        return head

    new = Node(d)
    new.next = temp.next
    temp.next = new

    return head

def display(head):
    t = head
    while t is not None:
        print(t.data, end="->")
        t = t.next
    print("None")
def db(head):
    if head is None:
        return head
    head=head.next
    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

display(head)

head = addafter(head, 55, 2)

display(head)
head=db(head)
display(head)
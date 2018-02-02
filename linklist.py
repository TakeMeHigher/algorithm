class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_linklist(li):
    head = None
    for num in li:
        node = Node(num)
        node.next = head
        head = node
    return head

def create_linklist_tail(li):
    head = None
    if not li:
        return head
    head = Node(li[0])
    tail = head
    for num in li[1:]:
        node = Node(num)
        tail.next = node
        tail = node
    return head


def print_linklist(head):
    node = head
    while node:
        print(node.data)
        node = node.next

linklist = create_linklist_tail([1,2,3,4])
print_linklist(linklist)
class Node(object):
    def __init__(self, val=0, next= None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
    
def build(values):
    dummy = Node()
    curr = dummy
    for v in values:
        node = Node(v)
        curr.next = node
        node.prev = curr
        curr = node
    head = dummy.next
    if head:
        head.prev = None
    return head

def show(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next 
    print()
    
def show_backward(tail):
    curr = tail
    while curr:
        print(curr.val , end=" ")
        curr = curr.prev
    print()

def get_tail(head):
    curr = head
    while curr.next:
        curr = curr.next
    return curr


def print_backward(head):
    curr = head
    while curr.next:
        curr = curr.next
    
    while curr:
        print(curr.val , end= " ")
        curr = curr.prev 
    print()

def insert_front(head, value):
    node = Node(value)
    node.next = head
    head.prev = node
    if head:
        head.prev = None
    return node 




    
tail = get_tail(build([1,2,3,4]))
print(tail.val)          # 4

print_backward(build([1,2,3]))    
show(insert_front(build([2,3]), 1))                  # 1 2 3
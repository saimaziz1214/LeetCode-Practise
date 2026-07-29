class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build(values):          # you already wrote this — reuse it
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def show(head):             # helper to print any list, reuse it
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()

def count(head):
    n = 0                 # counter — how many nodes we've seen so far
    curr = head           # finger starts at the front
    while curr:           # keep going until finger falls off the end (None)
        n = n + 1         # we're standing on a node, so count it
        curr = curr.next  # hop the finger to the next node
    return n  

def total(head):
    total = 0
    curr = head
    while curr:
        total = curr.val + total
        curr = curr.next
    return total

def biggest(head):
    big = head.val
    curr = head
    while curr:
        if curr.val> big:
            big = curr.val
        curr = curr.next
    return big


    
    
print(count(build([5, 9, 2])))   # 3
print(count(build([])))          # 0  (empty: curr is None immediately, loop never runs)
print(total(build([5, 9, 2])))
print(biggest(build([5, 9, 2, 7])) ) 
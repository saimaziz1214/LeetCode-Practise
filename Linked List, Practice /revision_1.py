class ListNode(object):
    def __init__(self, val=0, next= None):
        self.val=val
        self.next=next

def build (values):
    dummy=ListNode()
    curr= dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def show(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next 
    print()

def count_head(head):
    n = 0
    curr = head
    while curr:
        n = n+1
        curr = curr.next
    return n 

def total(head):
    curr = head
    total = 0
    while curr:
        total =curr.val + total
        curr = curr.next
    return total 

def biggest(head):
    curr = head
    big = head.val
    while curr:
        if curr.val>big:
            big = curr.val
        curr = curr.next
    return big

def contains(head, target):
    curr = head
    while curr:
        if curr.val == target:
            return True
        curr = curr.next
    return False 
     

def count_evens(head):
    n= 0
    curr = head
    while curr:
        if curr.val % 2 == 0:
            n = n + 1 
        curr= curr.next 
    return n 

def insert_front(head, value):
    node = ListNode(value)
    node.next = head 
    return node 

def insert_end(head, value):
    node = ListNode(value)
    curr = head 
    if head is None:
        return node 
        
    while curr.next :
        curr = curr.next 
    curr.next = node
    return head  
        
        
    
show(insert_end(build([5, 9]), 2))     # 5 9 2
show(insert_end(build([]), 2))         # 2
print(count_head(build([5, 9, 2])))    # 3
print(total(build([5, 9, 2])))         # 16
print(biggest(build([5, 9, 2, 7])))    # 9
print(contains(build([5, 9, 2]), 9))   # True
print(count_evens(build([5, 9, 2, 8])))# 2
    
    

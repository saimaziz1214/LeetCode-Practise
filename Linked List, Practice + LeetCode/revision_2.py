class ListNode(object):
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

def build(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def show(head):
    curr = head
    while curr:
        print(curr.val, end = " ")
        curr = curr.next
    print()
    
    
def count(head):
    curr = head
    n = 0
    while curr:
        n = n+1
        curr = curr.next
    return n

def total(head):
    curr = head
    total = 0
    while curr:
        total = curr.val + total
        curr = curr.next
    return total 
    
def contains(head, target):
    curr = head
    while curr:
        if curr.val == target:
            return True
        curr = curr.next
    return False  

def insert_front(head, value):
    node = ListNode(value)
    node.next = head
    return node

def insert_end(head, value):
    node = ListNode(value)
    curr = head
    if head is None:
        return head
    while curr.next:
        curr = curr.next
    curr.next = node
        
    return head 


def delete_value(head, target):
    curr = head
    while curr:
        if curr.next.val == target:
            curr.next=curr.next.next
            return head 
        curr = curr.next
    return head 
    
         
def copy_list(head):
    dummy = ListNode()
    curr = dummy
    walk = head
    while walk:
        curr.next = ListNode(walk.val)
        curr = curr.next
        walk = walk.next 
    return dummy.next
    
    
def double(head):
    dummy = ListNode()
    curr = dummy
    walk = head
    while walk :
        curr.next = ListNode(walk.val * 2)
        curr = curr.next
        walk = walk.next
    return dummy.next

def add_lists(a, b):
    dummy = ListNode()
    curr = dummy
    while a and b :
        curr.next = ListNode(a.val + b.val)
        curr = curr.next
        a = a.next
        b = b.next
    return dummy.next 

def merge(a,b):
    dummy = ListNode()
    curr = dummy
    while a and b:
        if a.val<= b.val:
            curr.next = a
            a = a.next
        else:
            curr.next = b
            b = b.next
        curr = curr.next
    curr.next = a if a else b
    return dummy.next

    
def merge_desc(a, b):
    dummy = ListNode
    curr = dummy
    while a and b:
        if a.val>= b.val:
            curr.next = a
            a = a.next
        else:
            curr.next = b
            b = b.next
        curr = curr.next
    curr.next  = a if a else b
    return dummy.next 


def interleave(a, b):
    dummy = ListNode()
    curr = dummy
    while a and b:
        curr.next = a
        a = a.next
        curr = curr.next
        curr.next = b
        
        b = b.next
        curr = curr.next
        
    curr.next = a if a else b
    return dummy.next 

    
    
        
        
        
        
        
        
print(count(build([5,9,2])))              # 3
print(total(build([5,9,2])))              # 16
print(contains(build([5,9,2]), 9))        # True
show(insert_front(build([9,2]), 5))       # 5 9 2
show(insert_end(build([5,9]), 2))         # 5 9 2
show(delete_value(build([5,9,2]), 9))     # 5 2
show(copy_list(build([5,9,2])))           # 5 9 2
show(double(build([5,9,2])))              # 10 18 4
show(add_lists(build([1,2,3]), build([10,20,30])))  # 11 22 33
show(merge(build([1, 3, 5]), build([2, 4, 6])))   # 1 2 3 4 5 6
show(merge(build([1, 2, 4]), build([1, 3, 4])))   # 1 1 2 3 4 4
show(merge(build([]), build([1, 2])))             # 1 2
show(merge_desc(build([5,3,1]), build([6,4,2])))    # 6 5 4 3 2 1
show(interleave(build([1,2,3]), build([7,8,9])))    # 1 7 2 8 3 9
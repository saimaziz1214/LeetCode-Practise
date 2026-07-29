class ListNode(object):
    def __init__(self, val = 0, next = None):
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
        print(curr.val , end= " ")
        curr = curr.next
    print()

def count(head):
    curr = head
    n = 0
    while curr:
        n = n + 1 
        curr = curr.next
    return n

def total(head):
    total = 0
    curr = head
    while curr:
        total = curr.val +total
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

def count_odds(head):
    curr = head
    odds = 0
    while curr:
        if curr.val % 2 !=0:
            odds = odds + 1
        curr = curr.next
    return odds

def insert_front(head, v ):
    node = ListNode(v)
    node.next = head 
    return node

def insert_end(head, v):
    node = ListNode(v)
    curr = head
    if head is None:
        return node
    
    while curr.next:
        curr = curr.next
    curr.next = node
    return head 
        
def delete_value(head, t):
    curr = head
    while curr:
        if curr.next.val == t:
            curr.next = curr.next.next
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

def triple(head):
    dummy = ListNode()
    curr = dummy
    walk = head
    while walk:
        curr.next = ListNode(walk.val * 3)
        curr = curr.next
        walk = walk.next
    return dummy.next

def add_five(head):
    dummy = ListNode()
    curr = dummy
    walk = head    
    while walk:
        curr.next = ListNode(walk.val + 5)
        curr = curr.next
        walk = walk.next
    return dummy.next

def add_lists(a,b):
    dummy = ListNode()
    curr = dummy
    while a and b:
        curr.next = ListNode(a.val + b.val)
        curr = curr.next
        a = a.next
        b = b.next
    return dummy.next

def merge(a,b):
    dummy = ListNode()
    curr = dummy
    while a and b:
        if a.val < b.val:
            curr.next = a
            a = a.next
            
        else:
            curr.next = b
            b = b.next
            
        curr = curr.next
    curr.next = a  if a else b 
    return dummy.next
        
def add_lists_carry(a,b):
    dummy = ListNode()
    curr = dummy
    carry = 0 
    while a or b or carry:
        v1 = a.val if a else 0
        v2 = b.val if b else 0
        total = v1+ v2+ carry
        digit = total% 10 
        carry = total //10
        
        curr.next = ListNode(digit)
        curr = curr.next
        
        if a: a = a.next
        if b: b = b.next
    return dummy.next 
    
    


print(count(build([5,9,2])))                        # 3
print(total(build([5,9,2])))                        # 16
print(biggest(build([5,9,2,7])))                    # 9
print(count_odds(build([5,9,2,7])))                 # 3
show(insert_front(build([9,2]),5))                  # 5 9 2
show(insert_end(build([5,9]),2))                    # 5 9 2
show(delete_value(build([5,9,2]),9))                # 5 2        
show(copy_list(build([5,9,2])))                     # 5 9 2
show(triple(build([5,9,2])))                        # 15 27 6
show(add_five(build([5,9,2])))                      # 10 14 7    
show(add_lists(build([1,2,3]),build([10,20,30])))   # 11 22 33
show(merge(build([1,3,5]),build([2,4,6])))          # 1 2 3 4 5 6
show(add_lists_carry(build([5,5]),build([5,5])))    # 0 1 1
show(add_lists_carry(build([9,9]),build([1])))      # 0 0 1        
show(add_lists_carry(build([9,9]), build([1])))       # 0 0 1   (99+1=100)
show(add_lists_carry(build([9,9,9]), build([1])))     # 0 0 0 1  (999+1=1000)
show(add_lists_carry(build([0]), build([7,3,5])))     # 7 3 5   (537+0=537)
show(add_lists_carry(build([2,4,3]), build([5,6,4]))) # 7 0 8
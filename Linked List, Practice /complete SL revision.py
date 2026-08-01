class ListNode(object):
    def __init__(self, val=0 , next= None):
        self.val = val
        self.next = next


def build(value):
    dummy = ListNode()
    curr = dummy
    for v in value:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def show(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()
    
def count(head):
    n = 0
    curr = head
    while curr:
        n = n+1
        curr = curr.next
    return n

def total(head):
    total = 0 
    curr = head
    while curr:
        total = total + curr.val
        curr = curr.next
    return total

def biggest(head):
    big = 0
    curr = head
    while curr:
        if curr.val>big:
            big = curr.val
        curr= curr.next
    return big 

def contains(head, value):
    curr = head
    while curr:
        if curr.val == value:
            return True
        curr = curr.next
    return False

def count_evens(head):
    n = 0
    curr = head
    while curr:
        if curr.val % 2==0:
            n = n+1
        curr = curr.next
    return n
    

def insert_front(head , v):
    node = ListNode(v)
    curr = head
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

def delete_value(head, v):
    curr = head
    while curr:
        if curr.next.val == v:
            curr.next = curr.next.next
        return head 
        curr= curr.next
    return head

def copy_list(head):
    dummy = ListNode()
    curr = dummy
    walk = head
    while walk:
        curr.next=ListNode(walk.val)
        curr = curr.next
        walk = walk.next
    return dummy.next

def double(head):
    dummy = ListNode()
    curr = dummy
    walk =head
    while walk:
        curr.next = ListNode(walk.val * 2)
        curr = curr.next
        walk = walk.next
    return dummy.next

def add_lists( a, b ):
    dummy = ListNode()
    curr = dummy
    while a and b:
        curr.next= ListNode(a.val + b.val)
        curr = curr.next
        a = a.next
        b = b.next
    return dummy.next
    
def merge(a,b):
    dummy =ListNode()
    curr = dummy
    while a and b:
        if a.val < b.val:
            curr.next = a
            a = a.next
        else:
            curr.next= b
            b= b.next
        curr = curr.next
    curr.next = a if a else b
    return dummy.next
            
def add_lists_carry(a,b):
    dummy = ListNode()
    curr = dummy
    carry= 0 
    while a or b or carry:
        v1= a.val if a else 0
        v2 = b.val if b else 0
        total = v1 + v2 + carry
        digit = total % 10
        carry = total//10
        
    
        curr.next = ListNode(digit)
        curr = curr.next
        
        if a: a = a.next
        if b: b = b.next
    return dummy.next 
        
# def middle(head):
#     n = 0
#     curr = head
#     while curr:
#         n = n+1
#         curr = curr.next
#     steps = n//2
#     curr = head
#     for i in range(steps):
#         curr = curr.next
#     return curr
        

def middle(head):
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow 
    
    
def hasCycle(head):
    fast= head
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast==slow:
            return True 
    
    return False 
    
def reverse(head):
    prev =None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev 
        
    

        

# ---- Traversal ----
# print(count(build([5,9,2])))                 # 3
# print(count(build([])))                      # 0
# print(total(build([5,9,2])))                 # 16
# print(biggest(build([5,9,2,7])))             # 9
# print(contains(build([5,9,2]), 9))           # True
# print(contains(build([5,9,2]), 4))           # False
# print(count_evens(build([5,9,2,8])))         # 2

# # # ---- Insert / delete ----
# show(insert_front(build([9,2]), 5))          # 5 9 2
# show(insert_front(build([]), 5))             # 5
# show(insert_end(build([5,9]), 2))            # 5 9 2
# show(insert_end(build([]), 2))               # 2
# show(delete_value(build([5,9,2]), 9))        # 5 2
# show(delete_value(build([5,9,2]), 99))       # 5 9 2  (not found, unchanged)

# # ---- Two-finger ----
show(copy_list(build([5,9,2])))              # 5 9 2
show(double(build([5,9,2])))                 # 10 18 4
show(add_lists(build([1,2,3]), build([10,20,30])))       # 11 22 33
show(merge(build([1,3,5]), build([2,4,6])))              # 1 2 3 4 5 6
show(merge(build([]), build([1,2])))                     # 1 2
show(add_lists_carry(build([5,5]), build([5,5])))        # 0 1 1
show(add_lists_carry(build([9,9]), build([1])))          # 0 0 1
show(add_lists_carry(build([2,4,3]), build([5,6,4])))    # 7 0 8

# # ---- Fast/slow ----
show(middle(build([1,2,3,4,5])))             # 3 4 5   (middle is 3)
show(middle(build([1,2,3,4,5,6])))           # 4 5 6   (middle is 4)

# # cycle detection (must wire the loop manually)
print(hasCycle(build([1,2,3,4])))            # False
# h = build([1,2,3,4]); h.next.next.next.next = h.next
# print(hasCycle(h))                           # True

# # ---- Three-finger ----
show(reverse(build([1,2,3])))                # 3 2 1
show(reverse(build([1,2,3,4,5])))            # 5 4 3 2 1
show(reverse(build([5])))                    # 5
show(reverse(build([])))                     # (empty line)
class ListNode(object):
    def __init__(self, val= 0, next= None):
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
    curr= head
    while curr:
        print(curr.val, end=" ")
        curr= curr.next
    print()
    
def copy_list(head):
    dummy = ListNode()
    curr = dummy
    walk = head
    while walk:
        curr.next = ListNode(walk.val)
        curr = curr.next
        walk= walk.next
    return dummy.next 

    

def add_ten(head):
    dummy = ListNode()
    curr = dummy
    walk = head
    while walk:
        curr.next = ListNode(walk.val + 10)
        curr = curr.next
        walk = walk.next
    return dummy.next

def double(head):
    dummy = ListNode()
    curr = dummy
    walk = head
    while walk:
        curr.next = ListNode(walk.val * 2)
        curr = curr.next
        walk= walk.next
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

        

def mul_lists(a,b):
    dummy = ListNode()
    curr = dummy
    while a and b:
        curr.next = ListNode(a.val * b.val)
        curr = curr.next
        a = a.next
        b = b.next
    return dummy.next

def max_lists(a,b):
    dummy = ListNode()
    curr = dummy
    while a and b:
        if a.val> b.val:
            curr.next = ListNode(a.val)
        else:
            curr.next = ListNode(b.val)
        curr = curr.next
        a = a.next
        b = b.next
    return dummy.next
        
    

show(copy_list(build([5, 9, 2])))     # 5 9 2
show(add_ten(build([5, 9, 2])))       # 15 19 12
show(double(build([5, 9, 2])))        # 10 18 4
# show(squares(build([2, 3, 4])))       # 4 9 16
# show(negate(build([5, -9, 2])))       # -5 9 -2
show(add_lists(build([1, 2, 3]), build([10, 20, 30])))   # 11 22 33
show(mul_lists(build([2,3,4]), build([10,10,10])))   # 20 30 40
show(max_lists(build([1,9,3]), build([5,2,8])))  

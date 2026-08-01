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
    
def delete(head, target):
    curr = head
    while curr:
        if curr.next.val == target:
            curr.next = curr.next.next
            return head 
        curr = curr.next
    return head 


print(show(delete(build([5, 9, 2]), 9)) )  # 5 2
# show(delete_value(build([5, 9, 2]), 2))   # 5 9
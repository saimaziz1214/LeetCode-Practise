class ListNode(object):
    def __init__(self, val=0, next=None):
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
            print (curr.val)
            curr = curr.next
        print()
        
def count_evens(head):
        curr = head
        n = 0
        while curr:
            if curr.val % 2 == 0:
                n = n+1
            curr = curr.next 
        return n 
    
def insert_end(head, value):
    curr = head 
    node = ListNode(value)
    if head is None:
        return node
        
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = node
    return head
    
    
    

    
# print(count_evens(build([1,2,3,4,5,6])))
show(insert_end(build([9, 2]), 5)) 
        
        
        
        
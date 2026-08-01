class Node(object):
    def __init__(self, val= 0 , next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
        
        
def dbuild(values):
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
    
def dshow(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()
    
def dshow_backward(tail):
    curr = tail
    while curr:
        print(curr.val, end=" ")
        curr = curr.prev
    print()
        
def get_tail(head):
    curr = head
    while curr.next:
        curr = curr.next 
    return curr 
    

def dinsert_front(head, value):
    node = Node(value)
    node.next = head
    
    if head :
        head.prev = node
    return node

def dinsert_end(head, value):
    node = Node(value)
    if head is None:
        return node
    curr = head
    while curr.next:
        curr = curr.next
    curr.next=node
    node.prev = curr
    return head 

def delete_value(head, target):
    curr = head
    while curr:
        if curr.val== target:
            if curr.prev:
                curr.prev.next = curr.next
            else:
                head = curr.next
            if curr.next:
                curr.next.prev = curr.prev
            return head
        curr = curr.next
    return head 

def move_to_front(head, node):
    if node is None:
        return head
    if node.prev:
       node.prev.next = node.next
    if node.next:
        node.next.prev = node.prev
    node.prev = None
    node.next = head
    head.prev = node
    return node
    
def remove_last(head):
    if head is None:
        return None
    if head.next is None:
        return None

    curr = head
    while curr.next:
        curr = curr.next
    curr.prev.next = None 
    
    
    return head
    
        

    
    
    
            
            

# ---- DL1: build + walk both ways ----
dshow(dbuild([1,2,3,4]))                      # 1 2 3 4
dshow_backward(get_tail(dbuild([1,2,3,4])))   # 4 3 2 1
print(get_tail(dbuild([1,2,3,4])).val)        # 4

# # ---- DL2: insert_front ----
dshow(dinsert_front(dbuild([2,3]), 1))        # 1 2 3
dshow(dinsert_front(dbuild([]), 1))           # 1
# # also verify backward after insert:
h = dinsert_front(dbuild([2,3]), 1)
dshow_backward(get_tail(h))                   # 3 2 1

# # ---- DL3: insert_end ----
dshow(dinsert_end(dbuild([1,2]), 3))          # 1 2 3
dshow(dinsert_end(dbuild([]), 3))             # 3
h = dinsert_end(dbuild([1,2]), 3)
dshow_backward(get_tail(h))                   # 3 2 1


# # ---- DL4: delete_value (middle, head, tail) ----
dshow(delete_value(dbuild([1,2,3]), 2))       # 1 3   (middle)
dshow(delete_value(dbuild([1,2,3]), 1))       # 2 3   (head)
dshow(delete_value(dbuild([1,2,3]), 3))       # 1 2   (tail)
dshow(delete_value(dbuild([1,2,3]), 9))       # 1 2 3 (not found)
# # verify backward still intact after a middle delete:
h = delete_value(dbuild([1,2,3,4]), 2)
dshow_backward(get_tail(h))                   # 4 3 1

# # ---- DL5: move_to_front (the LRU core move) ----
h = dbuild([1,2,3])
node3 = h.next.next                           # grab node holding 3
dshow(move_to_front(h, node3))                # 3 1 2
h = dbuild([1,2,3])
node2 = h.next                                # grab middle node
dshow(move_to_front(h, node2))                # 2 1 3

# # ---- DL6: remove_last (the LRU eviction move) ----
dshow(remove_last(dbuild([1,2,3])))           # 1 2
dshow(remove_last(dbuild([5])))               # (empty line)
        
        
    
class Node(object):
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class DLL(object):
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def show(self):                      # indented -> inside DLL
        curr = self.head.next
        while curr != self.tail:
            print(curr.val, end=" ")
            curr = curr.next
        print()

    def add_front(self, node):           # indented -> inside DLL
        first = self.head.next
        node.prev = self.head
        node.next = first
        self.head.next = node
        first.prev = node                # was self.tail.prev -> first.prev
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def remove_last(self):
       last= self.tail.prev   #last = head
       self.remove(last)
       return last

d = DLL()
d.add_front(Node(1)); d.add_front(Node(2)); d.add_front(Node(3))  # 3 2 1
print(d.remove_last().val)   # 1
d.show()                     # 3 2
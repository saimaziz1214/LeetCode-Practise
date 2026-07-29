# ---- test harness (build + show, just to run this locally) ----
# not part of the solution — LeetCode provides its own. this just lets me
# create a list, run my function, and print the result on my own machine.

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
        print(curr.val, end=" ")
        curr = curr.next
    print()

# ---- #237 Delete Node in a Linked List ----
# this one messed with my head because I'm NOT given the head — only the actual
# node to delete. so I can't do my usual thing of walking to the node before it
# and skipping over, because I have no way to reach whatever points AT this node.
# the trick: since I can't remove this node from the chain, I make it BECOME the
# next node instead. copy the next node's value into this one, then point past
# the next node. so the value I was told to delete is gone, and the list reads
# right — I basically deleted the next node while wearing this node's position.
# not really a pattern, more of a "you have to know the trick" problem.

class Solution(object):
    def deleteNode(self, node):
        node.val = node.next.val     # steal the next node's value into this one
        node.next = node.next.next   # then skip past the next node

# ---- run a local test ----
# note: LeetCode hands me the exact node to delete. to test locally I build a
# list, grab the node I want (e.g. the one holding 5), and pass THAT node in.
head = build([4, 5, 1, 9])
node_to_delete = head.next          # the node holding 5
Solution().deleteNode(node_to_delete)
show(head)                          # expected: 4 1 9
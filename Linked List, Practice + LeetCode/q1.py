# ============================================
# LINKED LIST PRACTICE — build it, feel it
# ============================================

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# --------------------------------------------
# EXERCISE 1: Build [5, 9, 2] BY HAND (no loop)
# --------------------------------------------
# Make three separate nodes, then link them with .next
# Then set `head` to the first node.

a = ListNode(5)       # node holding 5
b = ListNode(9)        # node holding 9
c = ListNode(2)       # node holding 2
a.next = b   # hook 5 -> 9
b.next = c   # hook 9 -> 2
head = a     # the front of the list

# --- print it to check (write this traversal yourself) ---
curr = head
while curr:
    print(curr.val)
    curr = curr.next
#
# Expected output:
# 5
# 9
# 2

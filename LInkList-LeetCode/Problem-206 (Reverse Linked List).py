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

# ---- #206 Reverse Linked List ----
# this one needs THREE fingers and it melted my brain at first. the whole
# problem is: I want to flip every arrow to point backward. but the second I
# do curr.next = prev, I've overwritten the arrow that pointed ahead — so if
# I didn't save the next node first, I'd lose the rest of the list.
# so the trick is: SAVE the next node before flipping. three pointers:
#   prev = the node behind me (what curr should now point back at), starts None
#   curr = the node I'm flipping right now, starts at head
#   nxt  = a temp save of the next node so I don't lose it
# four steps every loop, order matters: save ahead, flip backward, then shuffle
# both prev and curr forward.
# and I return PREV, not curr — when the loop ends curr is None, and prev is
# sitting on the last real node, which is the new head.

class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next      # 1. save the next node before we lose it
            curr.next = prev     # 2. flip: point this node backward
            prev = curr          # 3. move prev forward
            curr = nxt           # 4. move curr forward
        return prev              # prev is the new head

# ---- run LeetCode's test cases ----
sol = Solution()
show(sol.reverseList(build([1,2,3,4,5])))   # expected: 5 4 3 2 1
show(sol.reverseList(build([1,2])))         # expected: 2 1
show(sol.reverseList(build([])))            # expected: (empty line)

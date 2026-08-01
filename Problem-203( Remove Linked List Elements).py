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
# ---- #203 Remove Linked List Elements ----
# ok so this is just deleting nodes by value, but I kept failing one test case
# where the value to delete was right at the front. turns out my delete only
# ever looks at the NEXT node, so it literally can't kill the head. fix: stick
# a fake node in front of the head. now the head isn't special anymore — there's
# always something before it, so I can delete it like any other node.
# the other thing that bit me: after deleting, don't move forward! the new next
# node might also be a match (like a whole run of them). only move when I keep a node.
# at the end return dummy.next because the head might've changed.

class Solution(object):
    def removeElements(self, head, val):
        dummy = ListNode(0)      # fake node in front so the head isn't a special case
        dummy.next = head
        curr = dummy
        while curr.next:                    # keep going while there's a next node to check
            if curr.next.val == val:
                curr.next = curr.next.next  # skip it — but stay put, next one might match too
            else:
                curr = curr.next            # only move forward when we didn't delete
        return dummy.next        # head might've changed, so return dummy.next
    
    
    # ---- run LeetCode's test cases ----
sol = Solution()
show(sol.removeElements(build([1,2,6,3,4,5,6]), 6))   # expected: 1 2 3 4 5
show(sol.removeElements(build([]), 1))                # expected: (empty line)
show(sol.removeElements(build([7,7,7,7]), 7))         # expected: (empty line)
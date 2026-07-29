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

# ---- #876 Middle of the Linked List ----
# my idea here was the simple, obvious one: just count the whole list first,
# then walk halfway. so pass 1 walks through and counts how many nodes (n).
# then the middle is n//2 hops from the front. the nice thing is n//2 handles
# BOTH even and odd automatically — for odd it lands on the true middle, and
# for even it lands on the second middle, which is exactly what this problem wants.
# so no need for an if even/odd check.
# one thing I had to remember: after counting, curr is sitting at None (walked
# off the end), so I reset curr back to head before the second walk.
# there's a slicker one-pass fast/slow way too, but this two-pass version is
# the same O(n) and easier for me to reason about.

class Solution(object):
    def middleNode(self, head):
        curr = head
        n = 0
        while curr:               # pass 1: count all the nodes
            n = n + 1
            curr = curr.next
        steps = n // 2            # middle is n//2 hops in (works for even AND odd)
        curr = head               # reset to the front — curr was None after counting
        for i in range(steps):    # pass 2: walk to the middle
            curr = curr.next
        return curr

# ---- run LeetCode's test cases ----
sol = Solution()
show(sol.middleNode(build([1,2,3,4,5])))      # expected: 3 4 5
show(sol.middleNode(build([1,2,3,4,5,6])))    # expected: 4 5 6
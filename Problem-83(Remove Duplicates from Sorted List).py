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

# ---- #83 Remove Duplicates from Sorted List ----
# since the list is SORTED, any duplicates sit right next to each other. so I
# don't need to search or track anything — I just compare each node to the one
# right after it. if they're the same value, skip the next one.
# no dummy needed here (unlike #203) because the head never gets deleted — the
# first time a value shows up it always stays, only the repeats after it go.
# same skip-vs-move rule as before: when I delete, I stay put (there might be
# more of the same value ahead, like [1,1,1]). only move forward when the next
# value is different.
# and I loop on "while curr and curr.next" because I peek at curr.next.val — need
# to make sure that next node actually exists or it'd crash on the last node.

class Solution(object):
    def deleteDuplicates(self, head):
        curr = head
        while curr and curr.next:              # need a next node to compare against
            if curr.val == curr.next.val:      # same value? it's a duplicate
                curr.next = curr.next.next     # skip it — stay put, might be more
            else:
                curr = curr.next               # different value, move forward
        return head

# ---- run LeetCode's test cases ----
sol = Solution()
show(sol.deleteDuplicates(build([1,1,2])))        # expected: 1 2
show(sol.deleteDuplicates(build([1,1,2,3,3])))    # expected: 1 2 3
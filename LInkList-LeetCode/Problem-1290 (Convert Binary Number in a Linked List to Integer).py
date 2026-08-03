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

# ---- #1290 Convert Binary Number in a Linked List to Integer ----
# this is basically just my total/traversal, one finger walking the list, but
# instead of summing I'm building up a binary number.
# the trick I used: for each new bit, do n = n*2 + bit. multiplying by 2 shifts
# everything left one place (that's what shifting means in binary), then I add
# the new bit on the end. so [1,0,1] goes: 0 -> 1 -> 2 -> 5.
# no need to count the length or go backward or anything fancy — one pass, and
# I return the number n (NOT a node — got caught on that at first, kept returning
# the wrong thing).

class Solution(object):
    def getDecimalValue(self, head):
        n = 0
        curr = head
        while curr:
            n = (n * 2) + curr.val   # shift left by *2, then add the new bit
            curr = curr.next
        return n

# ---- run LeetCode's test cases ----
sol = Solution()
print(sol.getDecimalValue(build([1,0,1])))   # expected: 5
print(sol.getDecimalValue(build([0])))       # expected: 0

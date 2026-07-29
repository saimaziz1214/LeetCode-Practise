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

# ---- #2 Add Two Numbers ----
# this is basically my add_lists (two read-fingers walking l1 and l2 together
# and building a new list), but with the carry added on top. the digits are
# stored reversed (ones first) which is actually perfect — that's the order you
# add in by hand anyway, right to left.
# the carry was the part I had to really get. three lines: add both digits +
# carry, keep total % 10 as the digit, and total // 10 becomes the new carry.
# the KEY thing: carry = 0 goes BEFORE the loop so it survives between rounds —
# if I reset it inside, it'd never carry.
# two more things I needed: "or carry" in the while (so 5+5=10 still makes that
# leading 1 node even after both lists end), and v1 = l1.val if l1 else 0 so a
# shorter list just contributes 0 once it runs out. and the "if l1:" guards so
# I don't crash doing .next on None.

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        carry = 0                       # BEFORE the loop so it survives each round
        while l1 or l2 or carry:        # "or carry" so a leftover carry still gets a node
            v1 = l1.val if l1 else 0    # 0 if this list already ran out
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            digit = total % 10          # ones digit stays here
            carry = total // 10         # tens digit carries to the next round

            curr.next = ListNode(digit)
            curr = curr.next

            if l1: l1 = l1.next         # only hop if the list still has nodes
            if l2: l2 = l2.next
        return dummy.next

# ---- run LeetCode's test cases ----
sol = Solution()
show(sol.addTwoNumbers(build([2,4,3]), build([5,6,4])))   # expected: 7 0 8   (342+465=807)
show(sol.addTwoNumbers(build([0]), build([0])))           # expected: 0
show(sol.addTwoNumbers(build([9,9,9,9,9,9,9]), build([9,9,9,9])))  # expected: 8 9 9 9 0 0 0 1
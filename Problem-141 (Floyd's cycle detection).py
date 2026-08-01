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

# ---- #141 Linked List Cycle ----
# this is bascallyfast/slow two-pointer, after learning this i realized that i couldve done the problem (#876) the same way, 
# but i manage to do it through my own built algorithm, 
# so in this instead of stopping when fast hits the end, I watch for the two pointers
# to COLLIDE. slow moves 1 step, fast moves 2. on a straight list, fast just
# runs off the end and they never meet -> no cycle. but if the list loops,
# there's no end for fast to reach, so it keeps going around and eventually
# laps slow from behind -> they land on the same node -> cycle found.
# the key realisation: the only way fast can ever equal slow is if the list
# loops. so a collision IS proof of a cycle.
# return True the moment they meet; return False (outside the loop) only if
# fast escaped out the end.

class Solution(object):
    def hasCycle(self, head):
        fast = head
        slow = head
        while fast and fast.next:      # while fast can still hop 2
            slow = slow.next           # slow: 1 step
            fast = fast.next.next      # fast: 2 steps
            if fast == slow:           # same node? they collided -> cycle
                return True
        return False                   # fast hit the end -> no cycle

# ---- run a local test ----
# note: build() makes a normal (no-cycle) list. to test a cycle I have to
# wire the tail back to an earlier node myself.
print(Solution().hasCycle(build([1,2,3,4])))        # expected: False
h = build([1,2,3,4])
h.next.next.next.next = h.next                       # node 4 -> node 2 (loop)
print(Solution().hasCycle(h))                        # expected: True
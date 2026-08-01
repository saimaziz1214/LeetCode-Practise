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

    return dummy


head = build([5, 9, 2])

curr = head
while curr:
    print(curr.val)
    curr = curr.next
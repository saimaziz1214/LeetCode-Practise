# ---- #146 LRU Cache ----
# this was the big one — it's a doubly linked list + a hashmap working together.
# the idea: front of the list = most recently used, back = least recently used.
# every time I touch an item I move it to the front; when the cache is full I
# throw out whatever's at the back.
#
# the two structures split the work:
#   - the doubly linked list (DLL) tracks the ORDER — front recent, back old.
#     I used TWO dummy nodes (fake head + fake tail) so every real node always
#     has neighbours on both sides -> no edge-case "if" checks anywhere.
#   - the dict maps key -> node, so I can FIND any node instantly (O(1)) instead
#     of walking the list. it also holds every node's reference for me.
#
# each node stores its own key too — because when I evict from the back of the
# list, I also need to delete that key from the dict, so the node has to know
# which key it belongs to. dict and list always stay in sync: a node is in both
# or neither.
#
# get(key): dict finds the node -> move it to front -> return its value.
# put(key,value): if it exists, update + move to front. if it's new, add to
#   front + store in dict, and if that goes over capacity, evict the back node
#   and delete its key from the dict.

class Node(object):
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key            # node remembers its key (needed on eviction)
        self.val = val
        self.next = next
        self.prev = prev

class DLL(object):
    def __init__(self):
        self.head = Node()        # dummy head (fake bookend)
        self.tail = Node()        # dummy tail (fake bookend)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_front(self, node):    # insert right after dummy head
        first = self.head.next
        node.prev = self.head
        node.next = first
        self.head.next = node
        first.prev = node

    def remove(self, node):       # unhook — 2 lines, no guards (dummies!)
        node.prev.next = node.next
        node.next.prev = node.prev

    def remove_last(self):        # evict the node right before dummy tail
        last = self.tail.prev
        self.remove(last)
        return last


class LRUCache(object):
    def __init__(self, capacity):
        self.cap = capacity
        self.dic = {}             # key -> node (instant lookup)
        self.list = DLL()         # tracks usage order

    def get(self, key):
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self.list.remove(node)        # unhook from current spot
        self.list.add_front(node)     # move to front (just used)
        return node.val

    def put(self, key, value):
        if key in self.dic:                      # already there -> update + move
            node = self.dic[key]
            node.val = value                     # update the value!
            self.list.remove(node)
            self.list.add_front(node)
        else:                                    # brand new key
            node = Node(key, value)
            self.dic[key] = node
            self.list.add_front(node)
            if len(self.dic) > self.cap:         # over capacity -> evict
                last = self.list.remove_last()
                del self.dic[last.key]           # forget its key too


# ---- run LeetCode's test cases ----
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))    # 1
cache.put(3, 3)        # evicts key 2
print(cache.get(2))    # -1
cache.put(4, 4)        # evicts key 1
print(cache.get(1))    # -1
print(cache.get(3))    # 3
print(cache.get(4))    # 4

class ListNode:

    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    """
    T.C. : O(1) for get and put
    S.C. : O(1) for get and put, O(capacity) for the cache
    """

    def __init__(self, capacity):
        self.map = dict()
        self.capacity = capacity
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def deleteNode(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def insertAfterHead(self, node):
        nextNode = self.head.next
        self.head.next = node
        nextNode.prev = node
        node.prev = self.head
        node.next = nextNode

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        value = node.val
        self.deleteNode(node)
        self.insertAfterHead(node)
        return value

    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.deleteNode(node)
            self.insertAfterHead(node)
            return
        if len(self.map) == self.capacity:
            node = self.tail.prev
            del self.map[node.key]
            self.deleteNode(node)
        newNode = ListNode(key, value)
        self.map[key] = newNode
        self.insertAfterHead(newNode)

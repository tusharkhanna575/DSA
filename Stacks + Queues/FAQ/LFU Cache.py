class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.cnt = 1
        self.next = None
        self.prev = None


class List:

    def __init__(self):
        self.size = 0
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def addFront(self, node):
        temp = self.head.next
        node.next = temp
        node.prev = self.head
        self.head.next = node
        temp.prev = node
        self.size += 1

    def removeNode(self, delNode):
        prevNode = delNode.prev
        nextNode = delNode.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        self.size -= 1


class LFUCache:

    """
    T.C. : O(1) for get and put
    S.C. : O(1) for get and put, O(capacity) for the cache
    """

    def __init__(self, capacity):
        self.maxSizeCache = capacity
        self.minFreq = 0
        self.curSize = 0
        self.keyNode = dict()
        self.freqListMap = dict()

    def updateFreqListMap(self, node):
        del self.keyNode[node.key]
        self.freqListMap[node.cnt].removeNode(node)
        if (node.cnt == self.minFreq and self.freqListMap[node.cnt].size == 0):
            self.minFreq += 1
        nextHigherFreqList = List()
        if (node.cnt+1) in self.freqListMap:
            nextHigherFreqList = self.freqListMap[node.cnt+1]
        node.cnt += 1
        nextHigherFreqList.addFront(node)
        self.freqListMap[node.cnt] = nextHigherFreqList
        self.keyNode[node.key] = node

    def get(self, key):
        if key in self.keyNode:
            node = self.keyNode[key]
            value = node.value
            self.updateFreqListMap(node)
            return value
        return -1

    def put(self, key, value):
        if self.maxSizeCache == 0:
            return
        if key in self.keyNode:
            node = self.keyNode[key]
            node.value = value
            self.updateFreqListMap(node)
        else:
            if self.curSize == self.maxSizeCache:
                list = self.freqListMap[self.minFreq]
                del self.keyNode[list.tail.prev.key]
                self.freqListMap[self.minFreq].removeNode(list.tail.prev)
                self.curSize -= 1
            self.curSize += 1
            self.minFreq = 1
            listFreq = List()
            if self.minFreq and self.freqListMap:
                listFreq = self.freqListMap[self.minFreq]
            node = Node(key, value)
            listFreq.addFront(node)
            self.keyNode[key] = node
            self.freqListMap[self.minFreq] = listFreq

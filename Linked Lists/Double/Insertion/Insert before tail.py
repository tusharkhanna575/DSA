
# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Solution:

    def insertBeforeHead(self, head: ListNode, X: int) -> ListNode:
        # Your code goes here
        newHead = ListNode(X, None, head)
        if not head:
            return newHead
        head.prev = newHead
        return newHead

    def insertBeforeTail(self, head: ListNode, X: int) -> ListNode:
        # Your code goes here
        """
        T.C. : O(n)
        S.C. : O(1)
        """
        if not head:
            return ListNode(X)
        if (head.next == None):
            return self.insertBeforeHead(head, X)
        tail = head
        while (tail.next != None):
            tail = tail.next
        prev = tail.prev
        newNode = ListNode(X, prev, tail)
        prev.next = newNode
        tail.prev = newNode
        return head

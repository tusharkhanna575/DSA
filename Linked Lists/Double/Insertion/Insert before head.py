
# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Solution:
    def insertBeforeHead(self, head: ListNode, X: int) -> ListNode:
        # Your code goes here
        """
        T.C. : O(1)
        S.C. : O(1)
        """
        newHead = ListNode(X, None, head)
        if not head:
            return newHead
        head.prev = newHead
        return newHead


# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Solution:
    def insertBeforeGivenNode(self, node: ListNode, X: int) -> None:
        # Your code goes here
        """
        T.C. : O(1)
        S.C. : O(1)
        """
        prev = node.prev
        newNode = ListNode(X, prev, node)
        prev.next = newNode
        node.prev = newNode

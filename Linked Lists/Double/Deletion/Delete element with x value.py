
# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Solution:
    def deleteGivenNode(self, node: ListNode) -> None:
        # Your code goes here
        """
        T.C. : O(1)
        S.C. : O(1)
        """
        prev = node.prev
        front = node.next
        if (front == None):
            prev.next = None
            node.prev = None
            del node
            return
        prev.next = front
        front.prev = prev
        node.next = node.prev = None
        del node

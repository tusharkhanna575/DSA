# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Solution:
    def deleteHead(self, head: ListNode) -> ListNode:
        """
        T.C. : O(1)
        S.C. : O(1)
        """
        # Your code goes here
        if not head or head.next == None:
            return None
        prev = head
        head = head.next
        head.prev = None
        prev.next = None
        del prev
        return head

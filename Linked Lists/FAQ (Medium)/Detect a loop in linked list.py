# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head):
        """
        T.C. : O(n)
        S.C. : O(1)
        """
        slow, fast = head, head
        while ((fast != None) and (fast.next != None)):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

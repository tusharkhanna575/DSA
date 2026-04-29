# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head):
        """
        T.C. : O(n/2)
        S.C. : O(1)
        """
        if head == None or head.next == None:
            return None
        slow, fast = head, head.next.next
        while (fast != None and fast.next != None):
            fast = fast.next.next
            slow = slow.next
        if slow.next:
            slow.next = slow.next.next
        return head

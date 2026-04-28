# Definition for Singly Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        T.C. : O(n)
        S.C. : O(1)
        """
        slow, fast = head, head
        for i in range(n):
            fast = fast.next
        if fast == None:
            return head.next
        while (fast.next != None):
            slow = slow.next
            fast = fast.next
        delNode = slow.next
        del delNode
        slow.next = slow.next.next
        return head

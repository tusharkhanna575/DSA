# Definition for Singly Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleOfLinkedList(self, head):
        """
        T.C. : O(n)
        S.C. : O(1)
        """
        slow, fast = head, head
        while (fast != None and fast.next != None):
            fast = fast.next.next
            slow = slow.next
        return slow

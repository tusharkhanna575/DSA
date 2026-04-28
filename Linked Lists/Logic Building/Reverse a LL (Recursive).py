# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        """
        T.C. : O(n)
        S.C. : O(n)
        """
        if (head == None or head.next == None):
            return head
        newHead = self.reverseList(head.next)
        front = head.next
        front.next = head
        head.next = None
        return newHead

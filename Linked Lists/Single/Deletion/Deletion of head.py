# Definition of singly linked list:

class ListNode:
    def __init__(self, x=0, next=None):
        self.data = x
        self.next = next


class Solution:
    def deleteHead(self, head):
        """
        T.C. : O(1)
        S.C. : O(1)
        """
        # your code goes here

        if not head:
            return head
        temp = head
        head = head.next
        del temp
        return head

# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        """
        T.C. : O(n)
        S.C. : O(1)
        """
        temp = head
        prev = None
        while (temp != None):
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev

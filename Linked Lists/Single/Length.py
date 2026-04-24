# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def length(self, head):
        """
        T.C. : O(n)
        S.C. : O(1)
        """

        count = 0
        while head != None:
            count += 1
            head = head.next
        return count
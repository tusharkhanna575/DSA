# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseList(self, head):
        temp = head
        prev = None
        while (temp != None):
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev

    def addOne(self, head):
        """
        T.C. : O(n)
        S.C. : O(n)
        """

        def help(temp):
            if temp is None:
                return 1
            carry = help(temp.next)
            temp.val += carry
            if (temp.val < 10):
                return 0
            temp.val = 0
            return 1

        carry = help(head)
        if (carry == 1):
            return ListNode(1, head)
        return head

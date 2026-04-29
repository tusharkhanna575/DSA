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
        T.C. : O(3*n)
        S.C. : O(1)"""
        head = self.reverseList(head)
        temp = head
        carry = 1
        while (temp != None):
            temp.val += carry
            if (temp.val < 10):
                carry = 0
                break
            else:
                temp.val = 0
                carry = 1
            temp = temp.next
        head = self.reverseList(head)
        if (carry == 1):
            newNode = ListNode(1, head)
            return newNode
        return head

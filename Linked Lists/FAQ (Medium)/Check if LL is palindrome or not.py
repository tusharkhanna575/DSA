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

    def isPalindrome(self, head):
        """
        T.C. : O(2*n)
        S.C. : O(1)
        """
        slow, fast = head, head
        if (not head or not head.next):
            return True
        while (fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
        newHead = self.reverseList(slow.next)
        first = head
        second = newHead
        while second != None:
            if first.val != second.val:
                newHead = self.reverseList(newHead)
                return False
            first = first.next
            second = second.next
        newHead = self.reverseList(newHead)
        return True

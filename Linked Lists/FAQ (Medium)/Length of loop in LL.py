# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def findLength(self, slow, fast):
        cnt = 1
        fast = fast.next
        while (slow != fast):
            cnt += 1
            fast = fast.next
        return cnt

    def findLengthOfLoop(self, head):
        """
        T.C. : O(N)
        S.C. : O(1)
        """
        slow = fast = head
        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                return self.findLength(slow, fast)
        return 0

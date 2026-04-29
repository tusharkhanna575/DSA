# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA, headB):
        """
        T.C. : O(n1+n2)
        S.C. : O(1)
        """
        if (not headA or not headB):
            return None
        t1, t2 = headA, headB
        while (t1 != t2):
            t1 = t1.next
            t2 = t2.next
            if t1 == t2:
                return t1
            if t1 == None:
                t1 = headB
            if t2 == None:
                t2 = headA
        return t1

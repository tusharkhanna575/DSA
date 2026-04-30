# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        """
        T.C. : O(n+m) where n and m are the lengths of the two lists
        S.C. : O(1) as we are not using any extra space
        """
        t1, t2 = list1, list2
        dummy = ListNode(-1)
        temp = dummy
        while (t1 != None and t2 != None):
            if (t1.val < t2.val):
                temp.next = t1
                t1 = t1.next
            else:
                temp.next = t2
                t2 = t2.next
            temp = temp.next
        if (t1 != None):
            temp.next = t1
        else:
            temp.next = t2
        return dummy.next

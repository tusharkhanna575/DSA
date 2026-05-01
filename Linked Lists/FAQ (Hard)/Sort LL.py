# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head):
        """
        T.C. : O(nlogn)
        S.C. : O(logn) recursive stack space for merge sort + O(1) for merging two linked lists
        """
        if (head == None or head.next == None):
            return head
        mid = self.findMiddle(head)
        right = mid.next
        mid.next = None
        left = head
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge2LL(left, right)

    def findMiddle(self, head):
        slow = head
        fast = head.next
        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge2LL(self, list1, list2):
        dummy = ListNode(-1)
        temp = dummy
        while (list1 != None and list2 != None):
            if (list1.val < list2.val):
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        if list1:
            temp.next = list1
        else:
            temp.next = list2
        return dummy.next

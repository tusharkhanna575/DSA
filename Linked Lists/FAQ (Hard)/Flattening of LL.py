# Definiton of singly Linked List
class ListNode:
    def __init__(self, val=0, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child


class Solution:
    def flattenLinkedList(self, head):
        if (head is None or head.next is None):
            return head
        mergedHead = self.flattenLinkedList(head.next)
        head = self.merge(head, mergedHead)
        return head

    def merge(self, list1, list2):
        """
        T.C. : O(m * n^2) where n=> max. horizontal length and m=> max. vertical length
        S.C. : O(n) recursive stack space for flattening the linked list + O(1) for merging two linked lists
        """

        dummy = ListNode(-1)
        res = dummy
        while (list1 is not None and list2 is not None):
            if list1.val < list2.val:
                res.child = list1
                list1 = list1.child
            else:
                res.child = list2
                list2 = list2.child
            res = res.child
        if list1:
            res.child = list1
        else:
            res.child = list2
        if dummy.child:
            dummy.child.next = None
        return dummy.child

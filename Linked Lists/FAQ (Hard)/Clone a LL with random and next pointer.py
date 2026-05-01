# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


class Solution:

    def insertCopyInBetween(self, head):
        temp = head
        while temp:
            nextElement = temp.next
            copy = ListNode(temp.val)
            copy.next = nextElement
            temp.next = copy
            temp = nextElement

    def connectRandomPointers(self, head):
        temp = head
        while temp:
            copyNode = temp.next
            if temp.random:
                copyNode.random = temp.random.next
            else:
                copyNode.random = None
            temp = temp.next.next

    def getDeepCopyList(self, head):
        temp = head
        dummy = ListNode(-1)
        res = dummy
        while temp:
            res.next = temp.next
            res = res.next
            temp.next = temp.next.next
            temp = temp.next
        return dummy.next

    def copyRandomList(self, head):
        """
        T.C. : O(3*n) where n is the length of the linked list as we are traversing the linked list 3 times
        S.C. : O(n) for the new list we are creating
        """
        self.insertCopyInBetween(head)
        self.connectRandomPointers(head)
        return self.getDeepCopyList(head)

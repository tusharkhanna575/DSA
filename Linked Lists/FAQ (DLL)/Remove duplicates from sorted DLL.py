# Definition of doubly linked list:
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class Solution:
    def removeDuplicates(self, head):
        """
        T.C. : O(n) where n is the length of the linked list
        S.C. : O(1) as we are not using any extra space
        """
        temp = head
        while (temp != None and temp.next != None):
            nextNode = temp.next
            while (nextNode != None and nextNode.val == temp.val):
                duplicate = nextNode
                nextNode = nextNode.next
                del duplicate
            temp.next = nextNode
            if (nextNode != None):
                nextNode.prev = temp
            temp = temp.next
        return head

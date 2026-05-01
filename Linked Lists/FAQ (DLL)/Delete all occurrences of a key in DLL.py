# Definition of doubly linked list:
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class Solution:
    def deleteAllOccurrences(self, head, target):
        """
        T.C. : O(n) where n is the length of the linked list
        S.C. : O(1) as we are not using any extra space
        """
        temp = head
        while (temp != None):
            if (temp.val == target):
                if (temp == head):
                    head = temp.next
                nextNode = temp.next
                prevNode = temp.prev
                if (nextNode != None):
                    nextNode.prev = prevNode
                if (prevNode != None):
                    prevNode.next = nextNode
                del temp
                temp = nextNode
            else:
                temp = temp.next
        return head

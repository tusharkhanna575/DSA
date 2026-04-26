# Definition of singly linked list:
class ListNode:
    def __init__(self, x=0, next=None):
        self.data = x
        self.next = next


class Solution:
    def insertAtTail(self, head, x):
        """
            T.C. : O(n)
            S.C. : O(1) 
        """
        """
            :type head: Optional[ListNode]
            :type x: int
            :rtype: Optional[ListNode]
        """
        tail = ListNode(x)
        if not head:
            return tail

        temp = head
        while (temp.next != None):
            temp = temp.next
        temp.next = tail
        return head

# Definition of singly linked list:
class ListNode:
    def __init__(self, x=0, next=None):
        self.data = x
        self.next = next


class Solution:
    def oddEvenList(self, head):
        """
            :type head: Optional[ListNode]
            :rtype: Optional[ListNode]
        """
        """
            T.C. : O(n)
            S.C. : O(1)
        """
        if (not head or not head.next):
            return head

        odd = head
        even = head.next
        evenHead = head.next

        while (even != None and even.next != None):
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = evenHead
        return head

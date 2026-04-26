# Definition of singly linked list:
class ListNode:
    def __init__(self, x=0, next=None):
        self.data = x
        self.next = next


class Solution:
    def deleteTail(self, head):
        """
            T.C. : O(n)
            S.C. : O(1)
            :type head: Optional[ListNode]
            :rtype: Optional[ListNode]
        """
        if not head.next:
            return None
        temp = head
        while (temp.next != None and temp.next.next != None):
            temp = temp.next
        if temp.next.next == None:
            del temp.next.next
            temp.next = None
        return head

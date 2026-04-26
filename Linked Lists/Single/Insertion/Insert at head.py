# Definition of singly linked list:
class ListNode:
    def __init__(self, x=0, next=None):
        self.data = x
        self.next = next


class Solution:
    def insertAtHead(self, head, X):
        """
            T.C. : O(1)
            S.C. : O(1)
        """
        """
            :type head: Optional[ListNode]
            :type x: int
            :rtype: Optional[ListNode]
        """
        temp = ListNode(X)
        temp.next = head
        return temp

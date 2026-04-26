# Definition of singly linked list:
class ListNode:
    def __init__(self, x=0, next=None):
        self.data = x
        self.next = next


class Solution:
    def deleteNodeWithValueX(self, head, X):
        """
            T.C. : O(n)
            S.C. : O(1)
        """
        """
            :type head: Optional[ListNode]
            :type x: int
            :rtype: Optional[ListNode]
        """

        ans = ListNode(-1)
        ans.next = head
        temp = ans
        while temp.next:
            if temp.next.data == X:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return ans.next

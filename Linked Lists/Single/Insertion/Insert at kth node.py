# Definition of singly linked list:
class ListNode:
    def __init__(self, x=0, next=None):
        self.data = x
        self.next = next


class Solution:
    def insertAtKthPosition(self, head, X, k):
        """
            T.C. : O(n)
            S.C. : O(1)
        """
        """
            :type head: Optional[ListNode]
            :type x: int
            :rtype: Optional[ListNode]
        """

        newNode = ListNode(X)
        if not head:
            if k == 1:
                return newNode
            return None

        if k == 1:
            newNode.next = head
            return newNode

        cnt = 0
        temp = head
        while (temp != None):
            cnt += 1
            if cnt == (k-1):
                newNode.next = temp.next
                temp.next = newNode
                break
            temp = temp.next

        return head

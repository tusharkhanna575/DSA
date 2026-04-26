# Definition of singly linked list:
class ListNode:
    def __init__(self, x=0, next=None):
        self.data = x
        self.next = next


class Solution:
    def deleteKthNode(self, head, k):
        """
            T.C. : O(n)
            S.C. : O(1)
        """
        """
            :type head: Optional[ListNode]
            :type k: int
            :rtype: Optional[ListNode]
        """
        if head == None:
            return head
        if k == 1:
            temp = head
            head = head.next
            del temp
            return head
        cnt = 0
        temp, prev = head, None
        while (temp != None):
            cnt += 1
            if (cnt == k):
                prev.next = prev.next.next
                del temp
                break
            prev = temp
            temp = temp.next
        return head

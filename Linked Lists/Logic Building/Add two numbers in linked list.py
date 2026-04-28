# Definition of singly linked list:
class ListNode:
    def __init__(self, x=0, next=None):
        self.data = x
        self.next = next


class Solution:
    def addTwoNumbers(self, linkedList1, linkedList2):
        """
            :type linkedList1: Optional[ListNode]
            :type linkedList2: Optional[ListNode]
            :rtype: Optional[ListNode]
        """
        """
        T.C. : O(max(m,n))
        S.C. : O(1)
        """
        t1, t2 = linkedList1, linkedList2
        dummyNode = ListNode(-1)
        curr = dummyNode
        carry = 0
        while (t1 != None or t2 != None):
            sum = carry
            if t1:
                sum += t1.data
            if t2:
                sum += t2.data
            newNode = ListNode(sum % 10)
            carry = sum//10
            curr.next = newNode
            curr = curr.next
            if t1:
                t1 = t1.next
            if t2:
                t2 = t2.next
        if carry:
            newNode = ListNode(carry)
            curr.next = newNode
        return dummyNode.next

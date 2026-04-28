# Definition of singly linked list:
class ListNode:
    def __init__(self, x=0, next=None):
        self.data = x
        self.next = next


class Solution:
    def sortList(self, head):
        """
            :type head: Optional[ListNode]
            :rtype: Optional[ListNode]
        """
        """
            T.C. : O(n)
            S.C. : O(1)
        """
        if (head == None or head.next == None):
            return head
        head0 = ListNode(-1)
        head1 = ListNode(-1)
        head2 = ListNode(-1)
        zero, one, two = head0, head1, head2

        temp = head
        while (temp != None):
            if (temp.data == 0):
                zero.next = temp
                zero = temp
            elif (temp.data == 1):
                one.next = temp
                one = temp
            else:
                two.next = temp
                two = temp
            temp = temp.next
        if head1.next:
            zero.next = head1.next
        else:
            zero.next = head2.next
        one.next = head2.next
        two.next = None
        del zero, one, two
        return head0.next

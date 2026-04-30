# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head, k):
        """
        T.C. : O(n) where n is the length of the linked list
        S.C. : O(1) as we are not using any extra space
        """

        def getKthNode(temp, k):
            cnt = 1
            while (temp != None):
                if (cnt == k):
                    return temp
                cnt += 1
                temp = temp.next
            return temp

        if (head == None or k == 0):
            return head
        tail = head
        length = 1
        while (tail.next != None):
            tail = tail.next
            length += 1
        k %= length
        if (k == 0):
            return head
        tail.next = head
        newLast = getKthNode(head, length-k)
        head = newLast.next
        newLast.next = None
        return head

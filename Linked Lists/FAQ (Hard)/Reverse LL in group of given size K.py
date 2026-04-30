# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseList(self, head):
        temp = head
        prev = None
        while (temp != None):
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev

    def getKthNode(self, temp, k):
        while (temp != None and k > 1):
            k -= 1
            temp = temp.next
        return temp

    def reverseKGroup(self, head, k):
        """
        T.C. : O(n)
        S.C. : O(n) for recursive stack space
        """
        temp = head
        prevLast = None
        while (temp != None):
            kThNode = self.getKthNode(temp, k)
            if (kThNode == None):
                if prevLast:
                    prevLast.next = temp
                    break
            nextNode = kThNode.next
            kThNode.next = None
            newHead = self.reverseList(temp)
            if (temp == head):
                head = newHead
            else:
                prevLast.next = newHead
            prevLast = temp
            temp = nextNode
        return head

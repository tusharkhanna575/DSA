
# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Solution:

    def insertBeforeHead(self, head: ListNode, X: int) -> ListNode:
        # Your code goes here
        newHead = ListNode(X, None, head)
        if not head:
            return newHead
        head.prev = newHead
        return newHead

    def insertBeforeKthPosition(self, head: ListNode, X: int, K: int) -> ListNode:
        """
        T.C. : O(n)
        S.C. : O(1)
        """
        # Your code goes here
        temp = head
        cnt = 0
        while (temp != None):
            cnt += 1
            if (cnt == K):
                break
            temp = temp.next
        if (K == 1):
            return self.insertBeforeHead(head, X)
        prev = temp.prev
        newNode = ListNode(X, prev, temp)
        prev.next = newNode
        temp.prev = newNode
        return head

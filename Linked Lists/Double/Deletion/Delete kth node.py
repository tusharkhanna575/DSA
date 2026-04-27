
# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Solution:

    def deleteHead(self, head: ListNode) -> ListNode:
        # Your code goes here
        if not head or head.next == None:
            return None
        prev = head
        head = head.next
        head.prev = None
        prev.next = None
        del prev
        return head

    def deleteTail(self, head: ListNode) -> ListNode:
        # Your code goes here
        if not head or head.next == None:
            return None
        tail = head
        while (tail.next != None):
            tail = tail.next
        newTail = tail.prev
        newTail.next = None
        tail.prev = None
        del tail
        return head

    def deleteKthElement(self, head: ListNode, k: int) -> ListNode:
        # Your code goes here
        """
        T.C. : O(n)
        S.C. : O(1)
        """
        if not head:
            return None
        cnt = 0
        temp = head
        while (temp != None):
            cnt += 1
            if (cnt == k):
                break
            temp = temp.next
        prev = temp.prev
        front = temp.next
        if (prev == None and front == None):
            del temp
            return None
        elif (prev == None):
            return self.deleteHead(head)
        elif (front == None):
            return self.deleteTail(head)
        prev.next = front
        front.prev = prev
        temp.next = None
        temp.prev = None
        del temp
        return head

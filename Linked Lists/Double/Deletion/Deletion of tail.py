
# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def deleteTail(self, head: ListNode) -> ListNode:
        # Your code goes here
        """
        T.C. : O(n)
        S.C. : O(1)
        """
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

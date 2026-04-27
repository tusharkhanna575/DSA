"""
# Definition for a Node.
"""


class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Solution:
    def arrayToDoublyLinkedList(self, arr):
        """
        T.C. : O(n)
        S.C. : O(1)
        """
        # Your code goes here
        if not arr:
            return None
        head = ListNode(arr[0])
        prev = head
        for i in range(1, len(arr)):
            temp = ListNode(arr[i], prev, None)
            prev.next = temp
            prev = temp
        return head

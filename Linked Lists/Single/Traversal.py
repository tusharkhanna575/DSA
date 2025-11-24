# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def LLTraversal(self, head):
        ans = []
        while head != None:
            ans.append(head.val)
            head = head.next
        return ans
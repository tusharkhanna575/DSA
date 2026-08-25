# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:

    def floor(self, root, key):
        ans=-1
        curr=root
        while curr:
            if curr.data ==key:
                ans=curr.data
                break
            elif curr.data<key:
                ans=curr.data
                curr=curr.right
            else:
                curr=curr.left
        return ans


    def ceil(self, root, key):
        ans=-1
        curr=root
        while curr:
            if curr.data==key:
                ans=curr.data
                break
            elif curr.data>key:
                ans=curr.data
                curr=curr.left
            else:
                curr=curr.right
        return ans


    def floorCeilOfBST(self, root, key):
        #your code goes here
        ans=[-1,-1]

        ans[0]=self.floor(root, key)
        ans[1]=self.ceil(root, key)

        return ans
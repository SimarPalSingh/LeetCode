# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def helper(l,r):
            if l>r:
                return None
            
            midpoint = (l + r) //2
            root = TreeNode(nums[midpoint])
            root.left = helper(l, midpoint-1)
            root.right = helper(midpoint+1,r)

            return root
        return helper(0, len(nums)-1)
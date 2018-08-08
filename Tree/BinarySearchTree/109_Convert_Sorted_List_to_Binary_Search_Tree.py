# coding=utf-8

# 109. Convert Sorted List to Binary Search Tree
# 将有序数组转换为二叉树

# MyWay pre-order
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        length = len(nums)
        bst = TreeNode(nums[length/2])
        bst.left = self.sortedArrayToBST(nums[:length/2])
        bst.right = self.sortedArrayToBST(nums[length/2+1:])
        return bst

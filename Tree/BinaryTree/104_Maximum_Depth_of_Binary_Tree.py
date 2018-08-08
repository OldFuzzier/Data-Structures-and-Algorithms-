#
# coding=utf-8

# 104. Maximum Depth of Binary Tree
# 二叉树的最大深度

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# MyWay
class Solution(object):
    
    deep = 0
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, count):
            if not root:
                if count > self.deep:
                    self.deep = count
                return 
            dfs(root.left, count+1)
            dfs(root.right, count+1)
        dfs(root, 0)
        return self.deep
        

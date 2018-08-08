#
# coding=utf-8

# 112. Path Sum
# 路径总和

# MyWay: preorder + back tracking
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def backTracking(node, sum, temp):
            if not node:
                return False
            # prume
            # if temp+node.val > sum:
            #     return False
            if not(node.left or node.right) and temp+node.val == sum:
                return True
            # Trickier: 用逻辑表达式代替
            # equal 思想：先backTracking(left) 再backTracking(right) 最看他们之中有没有可以达到目标的
            return backTracking(node.left, sum, temp+node.val) or
                       backTracking(node.right, sum, temp+node.val)
        
        return backTracking(root, sum, 0)

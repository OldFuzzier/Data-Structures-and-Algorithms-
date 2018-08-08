#
# coding=utf-8

# 110. Balanced Binary Tree
# 平衡二叉树

# MyWay: backTracking(dfs)  good  complexity: O(n)
# compare every tree_node h(left) and h(right)
# not prume, but if prume, can improve performance  beat 81.99%
class Solution(object):
    ans = True
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # backTracking
        def back_tracking(root, deep):
            if not root:
                return deep
            hight_l = back_tracking(root.left, deep+1)
            hight_r = back_tracking(root.right, deep+1)
            if abs(hight_l - hight_r) > 1:
                self.ans = False
            return max(hight_l, hight_r)  # trickier: return hight of tree
        
        back_tracking(root, 0)
        return self.ans


# PCway: top-button  complexity: O(n2) 

# PCway: dfs+trickier button-top complexity O(n)
# exist prume -1, so proformance better than MyWay
# because height > 0, so the -1 can be a flag to prume
class Solution(object):

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs_height(root) != -1
    
    def dfs_height(self, root):
        if not root: return 0
        
        height_l = self.dfs_height(root.left)
        if height_l == -1: return -1  # trickier: prume
        height_r = self.dfs_height(root.right)
        if height_r == -1: return -1
        if abs(height_l-height_r) > 1: return -1
        
        return max(height_l, height_r) + 1


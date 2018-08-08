#
# coding=utf-8

# 235. Lowest Common Ancestor of a Binary Search Tree
# 二叉搜索树的最近公共祖先

# MyWay: p和q都左或都右
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:  # p == root.val or q == root.val:
            return root

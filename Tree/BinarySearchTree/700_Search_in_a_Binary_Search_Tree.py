#
# coding=utf-8

# 700. Search in a Binary Search Tree
# 二查搜索树的查询操作


# MyWay: recursion binary search
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root: return None
        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        elif root.val < val:
            return self.searchBST(root.right, val)


# PCWay: iterable binary search
# perfomance lower than MyWay
# but coding pretty
class Solution(object):
    def searchBST(self, root, val):
        while root and root.val != val:
            root = root.left if val < root.val else root.right
        return root

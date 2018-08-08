# 
# coding=utf-8

# 102. Binary Tree Level Order Traversal
# 二叉树层次遍历


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# MyWay BFS
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = [[root]] if root else []
        ansList = [[root.val]] if root else []
        while queue:
            root_list = queue.pop(0)
            ans = []
            for root in root_list:
                if root.left: ans.append(root.left)
                if root.right: ans.append(root.right)
            if ans:
                ansList.append(map(lambda root: root.val, ans))
                queue.append(ans)
        print ansList
        return ansList

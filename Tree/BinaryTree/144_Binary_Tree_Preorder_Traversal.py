#
# coding=utf-8

# 144. Binary Tree Preorder Traversal
# 前序遍历二叉树


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # MyWay: 队列前插
    # 每次需要新建list
    def preorderTraversal2(self, root):
        """              
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = [root] if root else []
        res_list = []
        while queue:
            temp = []
            node = queue.pop(0)
            if node.left: temp.append(node.left)
            if node.right: temp.append(node.right)
            queue = temp + queue  # Trickier: 队列前插
            res_list.append(node.val)
        return res_list
    
    # PCWay: 栈(right+left) goodway
    def preorderTraversal(self, root):
        stack = [root] if root else []
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            # Trickier: 为stack先添加right，再添加right从而达到preorder的效果
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        return res

print 123

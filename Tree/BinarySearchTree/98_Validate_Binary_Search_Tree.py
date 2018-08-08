# coding=utf-8

# 98. Validate Binary Search Tree
# 验证二叉树

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# in-order + compare element
# 此算法在排除最坏情况下，不需要遍历整棵树就能查询到是不是BST
class Solution(object):
    
    res = 1  # 1: true 0:false
    pre = ''  # previous temp
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        self.inorder(root)
        if self.res:
            return True
        else:
            return False
        
    
    def inorder(self, root):
        if not root or self.res == 0:  # reduce complex
            return
        self.inorder(root.left)
        if self.pre == '':  # border judge
            self.pre = root.val
        else:
            if self.pre >= root.val:  # compare element
                self.res = 0
            self.pre = root.val  # pass to previous pre
        self.inorder(root.right)


# PCWay
# "and" trickier
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def valid(node, lower, upper):
            if not node:
                return True
            if lower is not None and node.val <= lower:
                return False
            if upper is not None and node.val >= upper:
                return False
            # trickier:
            # equal to first a = valid(node.left, lower, node.val)
            # then b =  valid(node.right, node.val, upper)
            # final return a and b
            return valid(node.left, lower, node.val) \
                    and valid(node.right, node.val, upper)
        return valid(root, None, None)

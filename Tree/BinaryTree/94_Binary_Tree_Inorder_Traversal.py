# coding=utf-8

# 94. Binary Tree Inorder Traversal
# 中序遍历二叉树

# Solution: https://leetcode.com/articles/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# method1 recursive
class Solution(object):
    ansList = []
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorder(root):
            if not root:
                return
            self.inorder(root.left)
            self.ansList.append(root.val)
            self.inorder(root.right)
        inorder(root)
        return self.ansList


# method2 iterable
# stack store root.left
# 遇到一个结点，就把它推入栈中，并去遍历它的左子树。
# 遍历完左子树后，从栈顶托出这个结点并访问之，
# 然后按照它的右链接指示的地址再去遍历该结点的右子树。
class Solution2(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        ansList = []
        while root or stack:
            while root:  # trickier: stack store root.left
                stack.append(root)
                root = root.left
            root = stack.pop()
            ansList.append(root.val)
            root = root.right  # trickier: from root to root.right
        #　print ansList
        return ansList


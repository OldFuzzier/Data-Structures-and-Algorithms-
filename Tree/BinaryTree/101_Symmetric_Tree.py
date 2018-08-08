# coding=utf-8

# 101. Symmetric Tree
# 对称二叉树

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# MyWay in-order + 回文双指针检测
class Solution(object):
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        tempList = []  # store element
        def inorder(root):
            if not root or not (root.left or root.right):
                return 
            inorder(root.left)
            # in-order
            tempList.append(str(root.left.val)) if root.left else tempList.append('N')
            tempList.append(str(root.right.val)) if root.right else tempList.append('N')
            inorder(root.right)
        inorder(root)
        print tempList
        return self.isPalindrome(tempList)

    # double pointer
    def isPalindrome(self, lst):
        i, j = 0, len(lst)-1
        while i<j:
            if lst[i] == lst[j]:
                i += 1
                j -= 1
            else:
                return False
        return True


# PCWay
# "and" trickier
class Solution(object):
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:  # border situation
            return True
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, rootLeft, rootRight):
        if not rootLeft and not rootRight:  # have not branch
            return True
        if not rootLeft or not rootRight:  # lack a branch
            return False
        return (rootLeft.val == rootRight.val) \
                and self.isMirror(rootLeft.left, rootRight.right) \
                and self.isMirror(rootLeft.right, rootRight.left)  # trickier: acooding to symmetric tree


    

#
# coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 652. Find Duplicate Subtrees
# Solution: https://leetcode.com/articles/find-duplicate-subtrees/

from collections import defaultdict

class Solution(object):
    
    # PCway: serialize tree and counter subtree by Dict
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        ans_list = []
        counter_dict = defaultdict(int)
        def recursion(root):
            if not root: return '#'
            parttern = '%s, %s, %s' % (root.val, recursion(root.left), recursion(root.right))  # serialize tree
            counter_dict[parttern] += 1
            if counter_dict[parttern] == 2: ans_list.append(root)  # must ==2 not >1
            return parttern
        recursion(root)
        return ans_list
        

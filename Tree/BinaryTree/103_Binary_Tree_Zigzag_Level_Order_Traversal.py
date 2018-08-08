# coding=utf-8

# 103. Binary Tree Zigzag Level Order Traversal
# 二叉树的锯齿形层次遍历 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# MyWay: BFS(stack)+flag(ensure left or right)
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        stack = [root] if root else []  # create stack
        ansList = [[root.val]] if root else []
        flag = 0
        while stack:
            temp = []
            
            for _ in xrange(len(stack)):
                root = stack.pop()
                if flag:
                    if root.left:
                        stack.append(root.left)
                        temp.append(root.left.val)
                    if root.right:
                        stack.append(root.right)
                        temp.append(root.right.val)
                else:
                    if root.right:
                        stack.append(root.right)
                        temp.append(root.right.val)
                    if root.left:
                        stack.append(root.left)
                        temp.append(root.left.val)
                        
            if temp:
                ansList.append(temp)
                
            flag = 0 if flag else 1  1  # reverse flag

        return ansList


# PCWay: BFS + flag(trickier)
# Simple straightforward solution using flag to decide whether from left to right or from right to left
class Solution2(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res, temp, stack, flag=[], [], [root], 1
        while stack:
            for i in xrange(len(stack)):
                node=stack.pop(0)
                temp+=[node.val]
                if node.left: stack+=[node.left]
                if node.right: stack+=[node.right]
            res+=[temp[::flag]]  # # trickier:  reverse temp
            temp=[]
            flag*=-1  # trickier: reverse flag
        return res


#
# coding=utf-8

# 106. Construct Binary Tree from Inorder and Postorder Traversal
# 从后序和中序中构造二叉树


# PCWay
# postorder当做栈，pop出node，然后用node在inorder中分割
# trickier: postorder与inorder是同时吐出数据的, 所以不需要 and postorder
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder: # Trickier: and postorder:
            # print postorder
            # print inorder
            node_val = postorder.pop()
            node = TreeNode(node_val)
            index = inorder.index(node_val)
            node.right = self.buildTree(inorder[index+1:], postorder)  # right first
            node.left = self.buildTree(inorder[:index], postorder)  # left 
            return node


# MyWay 思路与PC一样
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder and postorder:
            node_val = postorder.pop()  # postorder必须每次都要pop
            if len(inorder) < 2:  # 当inorder里只有一个元素
                node = TreeNode(inorder[0])
                return node
            else:
                # print postorder
                # print inorder
                node = TreeNode(node_val)
                index = inorder.index(node_val)
                node.right = self.buildTree(inorder[index+1:], postorder)
                node.left = self.buildTree(inorder[:index], postorder)
                return node

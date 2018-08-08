# /usr/bin/python2.7
# coding=utf-8

# 105. Construct Binary Tree from Preorder and Inorder Traversal
# 从前序和中序中构造二叉树


# 使用前序找根，中序分割
class Solution(object):
    
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[index])
            root.left = self.buildTree(preorder, inorder[:index])
            root.right = self.buildTree(preorder, inorder[index+1:])
            return root

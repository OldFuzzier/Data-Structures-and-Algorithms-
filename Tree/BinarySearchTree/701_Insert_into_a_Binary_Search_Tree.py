#
# coding=utf-8

# 701. Insert into a Binary Search Tree
# 二叉搜索树的插入操作


# 默认方法：通过根据左右大小搜索到最末节点，然后进行插入
# prune 提升性能


# Myway+My_prune对PCway理解后 (good)
class Solution2(object):
    
    flag = False  # trickier: 通过flag进行剪枝
    
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if self.flag: return  # prune
        if not root:
            node = TreeNode(val)
            self.flag = True
            return node  # 不需要区分左右，可以对比另一种方法
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)  # Trickier write
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        return root
    

# MysWay: dfs+prune
class Solution(object):
    
    flag = False  # trickier: 通过flag进行剪枝
    
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def DFS(root, val, pre_root):
            if self.flag: return  # prime
            if not root:
                node = TreeNode(val)
                if val > pre_root.val:
                    pre_root.right = node
                elif val < pre_root.val:
                    pre_root.left = node
                self.flag = True
                return 
            if val < root.val:
                DFS(root.left, val, root)
            if val > root.val:
                DFS(root.right, val, root)
            
        DFS(root, val, None)
        return root


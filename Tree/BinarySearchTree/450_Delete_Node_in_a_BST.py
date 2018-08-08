#
# coding=utf-8

# 450. Delete Node in a BST
# 二查搜索树的删除操作

# 方法
# 1. 如果目标节点没有子节点，我们可以直接移除该目标节点 reture Null。
# 2. 如果目标节只有一个子节点，我们可以用其子节点作为替换 ex: root.left = root.left.left。
# 3. 如果目标节点有两个子节点，我们需要用其中序后继节点来替换，再进行deleteNode删除该目标节点。


# PCWay
# Trickier: Trickier way 与 Trickier write 都很重要
class Solution(object):

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: return 
        if key < root.val:
            root.left = self.deleteNode(root.left, key)  # Trickier write
        elif key > root.val:
            root.right = self.deleteNode(root.right, key) 
        else:  # key == root.val
            # have one child, meanwhile, have not child also use in here
            if not root.left:  # Trickier way, 不需要再去判断左右(记住)
                return root.right
            elif not root.right: 
                return root.left
            # have two child
            else:
                node = root.right  # 从右边开始inorder
                exchange_node = self.findMin(node)  # inorder到最后一个元素
                root.val = exchange_node.val  # replace
                root.right = self.deleteNode(root.right, exchange_node.val)   # delete replaced element
        return root
    
    def findMin(self, node):
        while node.left:
            node = node.left
        return node
            

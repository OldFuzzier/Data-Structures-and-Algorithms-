#
# coding=utf-8

# 173. Binary Search Tree Iterator
# 二叉搜索树迭代器


# PCWay:
# Trickier: stack store, stack.pop() is the smallest
class BSTIterator(object):
    
    # Your BSTIterator will be called like this:
    # i, v = BSTIterator(root), []
    # while i.hasNext(): v.append(i.next())
    
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0
        
    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()  # trickier: use stack take the smallest
        next_node = node.right
        while next_node:
            self.stack.append(next_node)
            next_node = next_node.left  # hold current smallest
        return node.val
        

#
# coding=utf-8

# 145. Binary Tree Postorder Traversal
# 后序遍历二叉树

# PCWay
# stack(node, right, left) + flag
# 
class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        traversal, stack = [], [(root, False)]  # trickier: (root, flag)
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    # add to result if visited
                    traversal.append(node.val)
                else:
                    # post-order
                    stack.append((node, True)) # trickier: sequence: 1.node
                    stack.append((node.right, False))  # 2.right
                    stack.append((node.left, False))  # 3.left

        return traversal


# PCWay clearWay
# https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/151213/Short-and-Simple-Python-Solution-beats-98.98
# dfs(node.right)+reverse
class Solution2(object):
    def postorderTraversal(self, root):
        ret, stack = [], root and [root]  # trickier written
        while stack:
            node = stack.pop()
            ret.append(node.val)
            stack += [child for child in (node.left, node.right) if child]
        return ret[::-1]

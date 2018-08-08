#
# coding:utf-8

# 236. Lowest Common Ancestor of a Binary Tree
# 二叉树最近公共祖先

class TreeNode(object):
    # Definition for a binary tree node.
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)

    def __eq__(self, other):
        return self.val == other.val


# MyWay 回溯(一次性双path)+剪枝+查找交叉点
class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        path_p, path_q = [], []
        def dfs(root, temp, path_p, path_q, p, q):
            # temp为路径，需要进行回溯
            # total_temp是总体list，不要要回溯
            # lst为两个node的容器，不需要回溯
            if path_p and path_q:  # trickier: 剪枝：当两个Node都找到，就不需要进行比较了
                return
            if not root:
                return
            if root == p:
                path_p.extend(temp)
                path_p.append(root)
            if root == q:
                path_q.extend(temp)
                path_q.append(root)
            temp.append(root)
            dfs(root.left, temp, path_p, path_q, p, q)
            dfs(root.right, temp, path_p, path_q, p, q)
            temp.pop()  # 回溯

        total_temp = dfs(root, [], path_p, path_q, p, q)
        lca = self.comparePath(path_p, path_q)
        # print lca
        return lca

    # 比较两个TreeNode的路径
    def comparePath(self, path_p, path_q):
        i = 0
        lca = None
        while i < len(path_p) and i < len(path_q):  # trikier: 不需要知道哪个list更短，只需要每回进行两次判断即可
            if path_p[i] == path_q[i]:
                lca = path_p[i]
            else:
                break
            i += 1
        return lca


# MyWay：回溯+剪枝+查找交叉点 memory excced
# 原理：分别找到连个node的path，然后对两个path进行对比，找到交叉点
# 需要对TreeNode进行重构，因为需要比较Node
class Solution1(object):

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def dfs(root, temp, total_temp, lst):
            # temp为路径，需要进行回溯
            # total_temp是总体list，不要要回溯
            # lst为两个node的容器，不需要回溯
            if not lst:  # trickier: 剪枝：当两个Node都找到，就不需要进行比较了
                return
            if not root:
                return
            if root in lst:
                total_temp.append(temp)
                lst.remove(root)
            dfs(root.left, temp + [root.left], total_temp, lst)
            dfs(root.right, temp + [root.right], total_temp, lst)
            return total_temp

        total_temp = dfs(root, [root], [], [p, q])
        lca = self.comparePath(total_temp)
        print lca
        return lca

    # 比较两个TreeNode的路径
    def comparePath(self, total_temp):
        i = 0
        lca = None
        lst1 = total_temp[0]
        lst2 = total_temp[1]
        while i < len(lst1) and i < len(lst2):  # trikier: 不需要知道哪个list更短，只需要每回进行两次判断即可
            if lst1[i] == lst2[i]:
                lca = lst1[i]
            else:
                break
            i += 1
        return lca

# test
# root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
# Solution1().lowestCommonAncestor(root, TreeNode(3), TreeNode(8))


# PCway 回溯(两次path)+剪枝+查找交叉点
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        pathp, pathq = [], []
        self.helper(root, p, [], pathp)
        self.helper(root, q, [], pathq)
        i = 0
        self.pathp, self.pathq = pathp[0], pathq[0]
        # compare the two paths one by one, until one goes out of range or the two don't equal
        while i < len(self.pathp) and i < len(self.pathq) and self.pathp[i] == self.pathq[i]:
            i += 1
        return self.pathp[i - 1]

    def helper(self, root, p, path, pathp):
        # put the final path into pathp
        if root is None:
            return
        if root == p:
            pathp.append(path + [p])
            return
        path.append(root)
        self.helper(root.left, p, path, pathp)
        self.helper(root.right, p, path, pathp)
        path.pop()


# PCway best
# 递归寻找两个带查询LCA的节点p和q，
# 当找到后，返回给它们的父亲。如果某个节点的左右子树分别包括这两个节点，
# 那么这个节点必然是所求的解，返回该节点。
# 否则，返回左或者右子树（哪个包含p或者q的就返回哪个）
class Solution3(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right

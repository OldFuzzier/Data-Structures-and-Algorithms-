#
# coding=utf-8

# 703. Kth Largest Element in a Stream(未解决)
# 一个序列对象中搜索第k大的对象

# leetcode提示:https://leetcode-cn.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/66/conclusion/182/
# leetcode解答: https://leetcode.com/problems/kth-largest-element-in-a-stream/discuss/155254/Java-BST-solution

        
# MyWay: 根据leetcode提示基本结构和流程都已实现，但其中有些规则不太懂
class MyBST(object):
    def __init__(self, val):
        self.val = val
        self.cnt = 1  # Trickier
        self.left = None
        self.right = None

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.root = MyBST(nums[0]) if nums else None
        for ele in nums[1:]:
            self.insertNode(self.root, ele)

    def insertNode(self, root, val):
        if not root:
            return MyBST(val)
        if val <= root.val:
            root.left = self.insertNode(root.left, val)
        else:
            root.right = self.insertNode(root.right, val)
        root.cnt += 1  # Trickier
        return root

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        def dfs(root):
            # Todo: need to known the thsis
            if root.right and self.k < root.right.cnt:
                return dfs(root.right)
            self.k = self.k - root.cnt - 1
            if self.k <= 0:
                return root
            else:   # elif self.k > 0:
                return dfs(root.left)
        self.insertNode(self.root, val)
        ans_root = dfs(self.root)
        return ans_root.val



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

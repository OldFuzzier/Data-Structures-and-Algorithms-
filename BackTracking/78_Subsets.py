# -*- coding: utf-8 -*-

# 78. Subsets
# 子集


#　my way BFS
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        out: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
        """
        outlist = []
        MaxLength = len(nums)
        count = 0
        def dfs(nums, count, temp):
            if len(temp) == count:
                outlist.append(temp)
                return
            for i in xrange(len(nums)):
                dfs(nums[i+1:], count, temp+[nums[i]])  # 回溯的方式选取
        while count <= MaxLength:
            # 分别从0-max来选取子集
            dfs(nums, count, [])
            count += 1
        return outlist


#　PC DFS good way
class Solution2(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        out: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
        """
        outlist = []
        def dfs(nums, temp):
            outlist.append(temp)
            for i in xrange(len(nums)):
                dfs(nums[i+1:], temp+[nums[i]])
        dfs(nums, [])
        return outlist

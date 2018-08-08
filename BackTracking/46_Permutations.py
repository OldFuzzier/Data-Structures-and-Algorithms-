# -*- coding: utf-8 -*-

# 46. Permutations
# 全排列


# my way
class Solution(object):
    temp = []

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        outputList = []

        def dfs(nums):
            if nums == []:
                outputList.append(self.temp)
                return
            # else:  作用等同于return
            for item in nums:
                self.temp.append(item)
                numsNew = nums[:]  # 新建了一个list，可以用索引取代
                numsNew.remove(item)
                self.temp = self.temp[:-1]  # 新建一个temp，并退回到上个步骤
        dfs(nums)
        return outputList


# pc，利用索引
class Solution2(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        outputList = []

        def dfs(nums, temp):
            if nums == []:
                outputList.append(temp)
                return
            # else:  作用等同于return
            for i in xrange(len(nums)):  # 利用索引
                # Params: nums[:i]+nums[i+1:]: 等同于新建一个list，去除里面的item
                # Params: temp+[nums[i]]: 将暂存的列表temp当做参数传送
                dfs(nums[:i]+nums[i+1:], temp+[nums[i]])
        dfs(nums, [])
        return outputList

# print Solution2().permute([1, 2, 3])

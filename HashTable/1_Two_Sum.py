#
# coding=utf-8

# 1.Two Sum

# PCway: One path hashmap, O(n)
# 主要思想: 主要通过一边遍历，一边在已有的hashmap中搜索
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        # build a map
        for i, num in enumerate(nums):
            rest = target - num
            if rest in d:
                return [d[rest], i]
            d[num] = i  # Trickier: 通过 d[nums] = index, 使后序seacrh O(1)


# PCway: Two path hashmap, O(n) + O(n)
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         d = {}
#         # build a map
#         for i, num in enumerate(nums):
#             d[num] = i  # Trickier: 通过 d[nums] = index, 使后序seacrh O(1)
#         # iterate nums
#         for i in xrange(len(nums)):
#             rest = target - nums[i]
#             if rest in d and d[rest] != i:
#                 return [i, d[rest]]
#         raise Exception        

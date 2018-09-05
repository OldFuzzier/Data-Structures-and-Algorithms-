#
# coding=utf-8

# 136. Single Number


# Myway: hashset, search in hashset O(1), then Time Complexity: O(n)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        for num in nums:
            if num in s:  # Trickier: use hashset: search O(1)
                s.remove(num)
                continue
            s.add(num)
        return s.pop()

# PCway: 两次for， 一次用dict计数，一次进行search
# class Solution(object):
#     def singleNumber(self, nums):
#         dic = {}
#         for num in nums:
#             dic[num] = dic.get(num, 0)+1
#         for key, val in dic.items():
#             if val == 1:
#                 return key

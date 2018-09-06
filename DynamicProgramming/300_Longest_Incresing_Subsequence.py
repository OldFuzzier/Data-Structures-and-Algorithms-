#
# coding=utf--8

# 300. Longest Increasing Subsequence
# 最长增长子序列

# 专业解答: https://leetcode.com/problems/longest-increasing-subsequence/solution/


class Solution(object):
    # DP O(n^2)
    # 基本思路：
    # 1 创建dp的table，一维list，每个i是第i个阶段
    # 2 每个阶段都要与之前子序列中的每一个值进行比较，包括current值下的最大长度值(不一定是最长的子序列)
    # 3 最后返回table的最长序列值 max(table)
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0  # border situation
        table = [1 for _ in xrange(len(nums))]  # 建table
        for i in xrange(1, len(nums)):
            max_ = 1
            for j in xrange(i):
                if nums[i] > nums[j]:  # 保证是升序
                    max_ = max(table[j]+1, max_)  # 返回最大的序列长度
            table[i] = max_  # 当前最大长度
        print table, max(table)  # test
        return max(table)

    # DP+BinarySearch O(nlogn)
    # 基本思路:
    # 1 创建DP的table，table是一个有序的序列
    # 2 遍历nums，num在table中进行二分搜索
    # 3 如果搜索位置是末尾，则table中添加num，否则替换table[binary_i]
    # 4 return len(table)
    def lengthOfLIS2(self, nums):
        # nums必须有序
        if not nums: return 0  # border
        table = []
        for num in nums:
            binary_i = self.binary_search(table, num)
            if binary_i > len(table) - 1:
                table.append(num)
            else:
                table[binary_i] = num
        print table, len(table)  # test
        return len(table)

    def binary_search(self, seq, num):
        start, end = 0, len(seq)-1
        while start <= end:
            mid = (start+end) / 2
            if seq[mid] > num:
                end = mid - 1
            elif seq[mid] < num:
                start = mid + 1
            else:
                return mid
        return start  # start == end



"""test"""
l = [1, 3, 6, 7, 9, 4, 10, 5, 6]
Solution().lengthOfLIS(l)

#
# coding=utf-8

# 387. First Unique Character in a String


class Solution(object):
    
    # MyWay: dict {key: counter}
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter_map = {}
        for ele in s:
            if ele in counter_map:
                counter_map[ele] += 1
            else:
                counter_map[ele] = 1
        for i in xrange(len(s)):
            if counter_map[s[i]] == 1:
                return i
        return -1

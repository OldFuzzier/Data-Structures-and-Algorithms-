#
# coding=utf-8

# 202. Happy Number

# PCway: check 重复 in set, 解决了死循环
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        while True:
            print n
            if n == 1: return True
            if n in s: return False  # Trickier
            s.add(n)
            n = sum(map(lambda x: int(x) ** 2, list(str(n))))

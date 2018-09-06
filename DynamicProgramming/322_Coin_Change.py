#
# coding=utf-8

# 322. Coin Change
# 硬币问题

# Solution: https://leetcode.com/problems/coin-change/solution/


class Solution(object):
    
    # PCway DP button-up
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount+1 for _ in xrange(amount+1)]  # init dp, 最大值设置为amount+1
        dp[0] = 0  # trickier: init first value, when 3-3=0
        for coin in coins:
            # every coin is a stage
            # update len(coins) status times
            # every use before status in current stage
            for num in xrange(1, amount+1):  # num is num and num index
                if num >= coin:
                    dp[num] = min(dp[num], dp[num-coin]+1)  # trickier: dp[coin-num]+1, when dp[6-3]=1 + 1 = 2
        # print dp  # test
        return dp[amount] if dp[amount] <= amount else -1

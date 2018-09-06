# 
# coding=utf-8

# 62. Unique Paths
# 不同路径


class Solution(object):
    
    # Myway dp
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in xrange(m+1)] for _ in xrange(n+1)]
        if len(dp)>=2: dp[1][0] = 1  # border
        for i in xrange(1, n+1):
            for j in xrange(1, m+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]  # trickier
        # print dp[n][m]
        return dp[n][m]
    
    # PCway dp better than me, but have not border
    def uniquePaths2(self, m, n):
        aux = [[1 for x in range(n)] for x in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                aux[i][j] = aux[i][j-1]+aux[i-1][j]
        return aux[-1][-1]  # Trickier
                
        

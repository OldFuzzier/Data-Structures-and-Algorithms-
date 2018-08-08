# coding=utf-8

# 22. Generate Parentheses
# 生成括号

# PCway
class Solution(object):
        
    def generateParenthesis(self, N):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:  # trickier num(right) < num(left)
                backtrack(S+')', left, right+1)

        backtrack()
        print ans
        return ans
    

# Mywany timeLimit Exceed
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ansList = []
        before = '('*n+')'*n
        def dfs(before, after, leftSum, rightSum, ansList):
            if not before and after not in ansList:
                # print after
                ansList.append(after)
                return 
            for i in xrange(len(before)):
                # judge "(" and ")" according to number("(")
                if leftSum < rightSum:
                    break
                ele = before[i]
                if ele=='(':
                    dfs(before[:i]+before[i+1:], after+ele, leftSum+1, rightSum, ansList)
                else:
                    dfs(before[:i]+before[i+1:], after+ele, leftSum, rightSum+1, ansList)
        dfs(before, '', 0, 0, ansList)
        # print ansList
        return ansList

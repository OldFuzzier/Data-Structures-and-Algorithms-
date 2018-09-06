#
# coding=utf-8

# 55. Jump Game
# 跳跃游戏

class Solution(object)

    # dp(Memory search) backtracking+memory
    # Time Limit Exceeded
    def canJump2(self, nums)
        
        type nums List[int]
        rtype bool
        
        length = len(nums)
        memo = ['' for _ in xrange(length)]  # init memory

        def backtracking(nums, index)
            if memo[index] and memo[index] == 'B' return False
            if index + nums[index] = length-1 return True
            for i in xrange(1, nums[index]+1)  # use to add
                if backtracking(nums, index+i) return True
            memo[index] = 'B'
            return False

        return backtracking(nums, 0)


print Solution().canJump([3,2,1,0,4])

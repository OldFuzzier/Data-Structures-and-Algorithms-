# /usr/bin/python
# coding=utf-8

# 17. Letter Combinations of a Phone Number
# 电话号码组合


class Solution(object):
    '''
    主要思路就是回溯dfs，用一个外部list进行储蓄每个结果。
    '''

    # count = 0  # count deep times
    strings = ''  # temp strings

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        charDict = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'],
                    '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'],
                    '8':['t','u','v'], '9':['w','x','y','z']}
        outputList = []
        inputLength = len(digits)
        def dfs():
            index = len(self.strings)  #  deep index
            if index == inputLength -1 :
                charList = charDict[digits[index]]
                for char in charList:
                    self.strings += char
                    outputList.append(self.strings)
                    self.strings = self.strings[:-1]
                return 
            # else: # 效果等同于return
            charList = charDict[digits[index]]
            for char in charList:
                self.strings += char  # self.count += 1
                dfs()
                self.strings = self.strings[:-1]  # self.count -= 1
        dfs()
        return outputList


# pc solution
class Solution2(object):

    def letterCombinations(self, digits):
        """
            :type digits: str
            :rtype: List[str]
            """
        res = []
        if not digits:
            return []
        dict = {"1": None, "2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"],
                "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"],
                "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}

        def dfs(digits, index, path, res):
            if index == len(digits):
                res.append(path)
                return
            for char in dict[digits[index]]:
                dfs(digits, index+1, path+char,res)  # 将索引和temp都放入参数中了，很好的设计
        dfs(digits, 0, '', res)
        return res



# print Solution2().letterCombinations('234')

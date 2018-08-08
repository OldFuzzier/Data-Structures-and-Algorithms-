# -*- coding: utf-8 -*-

# 79. Word Search
# 单词搜索


# my way
class Solution(object):

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rowLength = len(board)
        colLength = len(board[0])
        siteList = []  # 创建一个list，用于存储已用的单元格
        def dfs(board, word, siteList):
            if len(word) < 1:
                return True
            site = siteList[-1]  # 复制最后一个tuple作为位置
            left = (site[0], site[1]-1) if site[1]-1>=0 else None
            right = (site[0], site[1]+1) if site[1]+1<colLength else None
            up = (site[0]-1, site[1]) if site[0]-1>=0 else None
            down = (site[0]+1, site[1]) if site[0]+1<rowLength else None
            temp = [up, down, left, right]
            # print site, temp
            # print siteList
            # print '-------'
            for nextStep in temp:
                if nextStep and board[nextStep[0]][nextStep[1]]==word[0] and nextStep not in siteList:
                    # siteList.append(nextStep)
                    if dfs(board, word[1:], siteList+[nextStep]):
                        return True
                    # siteList.pop()
            return False

        for rowIndex in xrange(len(board)):
            for colIndex in xrange(len(board[rowIndex])):
                if board[rowIndex][colIndex] == word[0]:
                    # siteList.append((rowIndex, colIndex))
                    if dfs(board, word[1:], siteList+[(rowIndex, colIndex)]):
                        return True
                    # siteList.pop()
        else:
            return False


# pc way 相比于我的方法，少创建了一个list，但思路不如我的好记
class Solution2(object):
    def exist(self, board, word):
        if not word:
            return True
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.exist_helper(board, word, i, j):
                    return True
        return False

    def exist_helper(self, board, word, i, j):
        if board[i][j] == word[0]:
            if not word[1:]:
                return True
            board[i][j] = " "  # indicate used cell
            # check all adjacent cells
            if i > 0 and self.exist_helper(board, word[1:], i - 1, j):
                return True
            if i < len(board) - 1 and self.exist_helper(board, word[1:], i + 1, j):
                return True
            if j > 0 and self.exist_helper(board, word[1:], i, j - 1):
                return True
            if j < len(board[0]) - 1 and self.exist_helper(board, word[1:], i, j + 1):
                return True
            board[i][j] = word[0]  # update the cell to its original value
            return False
        else:
            return False


# board = [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# board2 = [["C","A","A"],["A","A","A"],["B","C","D"]]
#
#
# word = 'ABCCED'
# word2 = 'SEE'
# word3 = "ABCB"
# word4 = "AAB"

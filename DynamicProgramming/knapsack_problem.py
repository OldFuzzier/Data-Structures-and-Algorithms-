#
# coding=utf-8

# 背包问题
# 基础讲解: http://www.importnew.com/13072.html
# 代码描述: https://www.jianshu.com/p/25f4a183ede5

#
# coding=utf-8


class Solution(object):

    def assign(self, capacity, value, weight):
        """
        :param capacity:  backpack capacity integer
        :param worth: array of item worth
        :param weight: array of item weight
        :return: the max worth integer
        """
        # x: stage;
        # y: status
        table = [[0 for _ in xrange(capacity+1)] for _ in xrange(len(value))]
        # i: item index;
        # c: current capacity and current capacity index
        for i in xrange(1, len(value)):
            for c in xrange(1, capacity+1):
                if weight[i] <= c:
                    table[i][c] = max(value[i]+table[i-1][c-weight[i]], table[i-1][c])
                else:
                    table[i][c] = table[i-1][c]  # 返回上一个阶段的状态
        self.print_table(table)  # 将动态规划表打印出来
        return table[len(value)-1][capacity]

    def print_table(self, table):
        for stage in table:
            print stage


value = [0, 10, 40, 30, 50]
weight = [0, 5, 4, 6, 3]
Solution().assign(10, value, weight)

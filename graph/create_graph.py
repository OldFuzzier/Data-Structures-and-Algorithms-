#
# coding=utf-8

from collections import defaultdict


def build_graph_matrix():
    # 二维数据表结构
    # [[dist(1,1), dist(1,2)], [dist(2,1), dist(2,2), ...]
    # graph[v1][v2]
    lst = map(lambda x: int(x), raw_input().split())
    n_v, n_e = lst[0], lst[1]
    # init graph
    graph = [[0 for _ in xrange(0, n_v)] for _ in xrange(0, n_v)]
    # insert edge
    for _ in xrange(n_e):
        lst = map(lambda x: int(x), raw_input().split())
        v1, v2, w = lst[0], lst[1], lst[2]
        graph[v1][v2] = w
        # graph[v2][v1] = w 无向图时需要
    return graph


def build_graph_table():
    # 二维数据字典结构
    # {'A':{'B':12, 'C':7}, 'B':{'C':5}, 'C':{}}
    # table['A']['B']
    lst = map(lambda x: int(x), raw_input().split())
    n_v, n_e = lst[0], lst[1]
    # init graph
    graph = defaultdict(dict)
    # insert edge
    for _ in xrange(n_e):
        lst = map(lambda x: int(x), raw_input().split())
        v1, v2, w = lst[0], lst[1], lst[2]  # default w=1
        graph[v1][v2] = w
    return graph



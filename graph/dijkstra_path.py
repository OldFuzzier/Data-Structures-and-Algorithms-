#
# coding=utf-8

# dijkstra加权(有)无向图最短路径
# trickier: 每次通过 dist获取当前最短距离的vector；用collection控制能否选择该vector

from collections import defaultdict

# init
graph = defaultdict(dict)
graph[1][2] = 1
graph[1][3] = 12
graph[2][3] = 9
graph[2][4] = 3
graph[3][5] = 5
graph[4][3] = 4
graph[4][5] = 13
graph[5][6] = 4
graph[4][6] = 15
dist = dict.fromkeys([point for point in range(1, 7)], 9999999)
path = dict.fromkeys([point for point in range(1, 7)], 'N')
collection = dict.fromkeys([point for point in range(1, 7)], True)


# dijkstra
def dijkstra_path(s):
    # params: s: source
    dist[s] = 0  # update source
    while True:
        v = min_path(dist)  # 每次选出当前条件下的最短路径点
        if not v:  # 如果所有点都被处理就中断操作
            break
        collection[v] = False  # 该点已经被访问
        for w in graph[v]:  # w是v能到达的点
            if collection[w] and dist[w] > dist[v] + graph[v][w]:
                # min(dist[w], dist[v]+table[v][w]
                dist[w] = dist[v] + graph[v][w]  # update dist
                path[w] = v  # update path

def min_path(dist):
    min_ = 9999999
    min_point = None
    for k in dist:
        if collection[k] and dist[k] < min_:  # 该点未被访问且在当前条件下距离最小
            min_ = dist[k]
            min_point = k
    return min_point


if __name__ == '__main__':
    dijkstra_path(1)
    # shortest distance
    print dist
    # shortest path
    stack = [6]  # add end
    v = stack[-1]
    while path[v] != 1:
        v = path[v]
        stack.append(v)
    stack.append(1)# add head
    print stack


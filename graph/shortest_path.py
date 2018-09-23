#
# coding=utf-8

# 无权图有(无)向最短路径

from collections import defaultdict

# init
graph = defaultdict(dict)
graph[1][2] = 1
graph[1][3] = 1
graph[2][3] = 1
graph[2][4] = 1
graph[3][5] = 1
graph[4][3] = 1
graph[4][5] = 1
graph[5][6] = 1
graph[4][6] = 1
dist = dict.fromkeys([point for point in range(1, 7)], -1)
path = dict.fromkeys([point for point in range(1, 7)], 'N')


# bfs改进
def shortest_path(s):
    # params: s: 起始点
    queue = [s]
    dist[s] = 0
    while queue:
        v = queue.pop(0)
        for w in graph[v]:  # w是v能到达的点
            if dist[w] == -1:  # dist[w]默认都为-1表示未访问过
                dist[w] = dist[v] + graph[v][w]  # graph[v][w]==1
                path[w] = v  # 记录w的上一个点是v
                queue.append(w)


if __name__ == '__main__':
    shortest_path(1)
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
    

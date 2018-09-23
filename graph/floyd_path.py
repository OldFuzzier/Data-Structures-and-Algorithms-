#
# coding=utf-8


# 多源路问题如果应用dijikstra算法解决的话，需要对每一个vector都用一遍，
# 所以算法整体复杂度为 o(v*(v^2+e)) > o(v^3),
# 而如果用floyd算法的话，复杂度为 o(v^3)

# floyd最短路径算法，解决多源有(无)项图最短路径问题
# 核心思想类似于dp, graph[i][j]=min(graph[i][k]+graph[k][j], graph[i][j])
# 判断有无中间vector k使图中某段距离更新


from collections import defaultdict

# init vector序列
vector_list = range(0, 7)  #need: 1, 2, 3, 4, 5, 6

# init 这里需要创建图矩阵
def init_graph():
    # return: graph: graph_matrix
    graph = []
    path = []
    for raw in vector_list:
        graph.append([])
        path.append([])
        for col in vector_list:
            if raw == col:
                graph[raw].append(0)
            else:
                graph[raw].append(999999)
            path[raw].append(-1)  # 这里需要定义为-1

    graph[1][2] = 1
    graph[1][3] = 12
    graph[2][3] = 9
    graph[2][4] = 3
    graph[3][5] = 5
    graph[4][3] = 4
    graph[4][5] = 13
    graph[5][6] = 4
    graph[4][6] = 15
    return graph, path


graph, path = init_graph()


# floyd最短路径算法
def floyd_path():
    # params: s: source
    for k in vector_list:  # 允许插于的中间的vector
        for i in vector_list:
            for j in vector_list:
                if graph[i][j] > graph[i][k]+graph[k][j]:
                    graph[i][j] = graph[i][k]+graph[k][j]
                    path[i][j] = k  # i到j的最短距离必经的点


# 查找最短路径
# 以k划分，递归查找
def shortest_path(s, e):
    # params: s: source
    # params: e: end
    k = path[s][e]
    if k == -1: return [e]
    return shortest_path(s, k) + shortest_path(k, e)


if __name__ == '__main__':
    floyd_path()
    print graph
    path_temp = shortest_path(1, 6)
    path_temp.insert(0, 1)  # 插入第一个vector
    print path_temp

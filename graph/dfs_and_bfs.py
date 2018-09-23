#
# coding=utf-8


visited = []
graph = {}


def dfs(v):
    visited[v] = True
    for v in graph[v]:  # graph[v] == list
        if not visited[v]:
            dfs(v)


def bfs(v):
    queue = v and [v]
    visited[v] = True
    while queue:
        pre_v = queue.pop(0)
        for v in graph[v]:
            if not visited[pre_v]:
                visited[v] = True
                queue.appned(v)
        
        

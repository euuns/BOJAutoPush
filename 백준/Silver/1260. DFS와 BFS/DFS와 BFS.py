from collections import deque
import sys

# 너비 우선 탐색
def BFS(Graph, start):
    visited[start] = True
    que = deque([start])

    while que:
        u = que.popleft()
        print(u, end=' ')

        for i in Graph[u]:
            if not visited[i]:
                visited[i] = True
                que.append(i)

# 깊이 우선 탐색
def DFS(Graph, start):
    visited[start] = True
    print(start, end=' ')

    for i in Graph[start]:
        if not visited[i]:
            DFS(Graph, i)


N, M, V = map(int, sys.stdin.readline().split())
# N(정점의 개수), M(간선의 개수), V(정점의 번호)

graph = [ [] for x in range(N+1) ]
visited = [False] * (N+1)
# 각 인덱스 번호 = 노드의 번호
# 각 인덱스의 원소 = 노드에 연결된 다른 노드

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a] += [b]
    graph[b] += [a]
# 무향 그래프로 서로 양방향으로 연결되어 있다.

for i in graph:
    i = i.sort()
# 정점의 번호가 작은 것을 먼저 방문하기 위해 오름차순 정렬


DFS(graph,V)
print()

visited = [False] * (N+1)
# DFS 연산 후 visited의 요소값이 바뀌었기 때문에
# BFS 연산을 위해 방문값을 처음으로 되돌려 준다.
BFS(graph,V)
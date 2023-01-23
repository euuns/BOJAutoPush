from collections import deque
import sys

n = int(sys.stdin.readline())   # 노드의 수
m = int(sys.stdin.readline())   # 연결된 노드
graph = [ [] for x in range(n+1)]
visited = [False] * (n+1)
# 1번 컴퓨터에서 시작해 7번 컴퓨터까지 표시하기 위해 +1을 진행
# ==> 0번부터 7번까지 생성되어 1번 인덱스부터 사용

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a] += [b]
    graph[b] += [a]
    # 무향 그래프 생성 => 서로 연결

def BFS(Graph, start):
    deq = deque([start])
    visited[start] = True

    while deq:
        v = deq.popleft()
        for i in Graph[v]:
            if not visited[i]:
                visited[i] = True
                deq.append(i)

BFS(graph, 1)

print(visited.count(True)-1)
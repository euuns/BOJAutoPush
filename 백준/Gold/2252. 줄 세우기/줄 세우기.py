from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
# n = 학생 수 = 노드 / m = 비교 횟수 = 간선
graph = [ [] for x in range(n+1)]
indegree = [0] * (n+1)  # (인덱스 번호 = 노드)의 진입간선 수를 저장

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a] += [b]
    indegree[b] += 1
    # a -> b 로 이동, indegree는 진입간선 수를 저장 = 진입된 b 증가

def topologySort(Graph):
    Q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            Q.append(i)
    # 진입간선이 없는 노드 큐에 삽입

    while Q:
        now = Q.popleft()
        print(now, end=' ')
        for i in Graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                Q.append(i)

topologySort(graph)


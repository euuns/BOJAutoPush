import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
li = [ [] for x in range(n+1) ]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    li[a] += [b]
    li[b] += [a]

visited = [False] * (n+1)
def BFS(Graph, start):
    deq = deque([start])
    visited[start] = True

    while deq:
        v = deq.popleft()
        for i in Graph[v]:
            if not visited[i]:
                visited[i] = True
                deq.append(i)

cnt = 0
for i in range(1, len(visited)):
    if not visited[i]:
        BFS(li,i)
        cnt += 1

print(cnt)
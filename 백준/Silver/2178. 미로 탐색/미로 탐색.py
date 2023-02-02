import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = []
for i in range(N):
    graph.append(list(map(int,sys.stdin.readline().strip())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
# 상하좌우로 이동할 방향 지정

# x,y부터 시작해 방향 탐색
def BFS(x,y):
    q = deque([(x, y, 1)])
    # 이동 칸 수를 나타낼 cnt, 첫 탐색 1부터 시작

    while q:
        # x와 y 좌표를 now에 언패킹
        now_x, now_y, cnt = q.popleft()
        
        if now_x == N-1 and now_y == M -1:
            break

        # 위치 확인은 상하좌우 = 4번 반복
        for i in range(4):
            # 현재 위치에서 다음 위치를 탐색
            check_x = now_x + dx[i] # 행
            check_y = now_y + dy[i] # 열

            # 각 좌표가 미로 범위를 벗어나지 않도록 조건 추가, 벗어날 경우 continue
            if (check_x < 0) or (check_x >= N) or (check_y < 0) or (check_y >= M):
                continue

            # 1이 쓰여진 칸만 이동할 수 있다
            if graph[check_x][check_y] == 1:
                graph[check_x][check_y] = graph[now_x][now_y] + 1
                q.append((check_x, check_y, cnt+1))
    
    print(cnt)

BFS(0,0)
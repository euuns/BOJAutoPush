import sys

# N개의 로프
N = int(sys.stdin.readline())

k = []
w = []

for _ in range(N):

    # 로프가 버틸 수 있는 최대 중량
    k.append(int(sys.stdin.readline()))

k.sort(reverse=True)

# 나누어서 들 수 있는 각 중량을 w에 저장
for i in range(N):
    w.append(k[i]*(i+1))

# 최대 중량 출력
print(max(w))
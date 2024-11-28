import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

seonsor = list(map(int, sys.stdin.readline().split()))
seonsor.sort()

distance = []
for i in range(N-1):
    distance.append(seonsor[i+1] - seonsor[i])
distance.sort(reverse=True)

print(sum(distance[K-1:]))
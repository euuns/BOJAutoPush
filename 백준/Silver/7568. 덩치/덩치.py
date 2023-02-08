import sys
N = int(sys.stdin.readline())
X = []

for i in range(N):
    weight, height = map(int, sys.stdin.readline().split())
    X.append([weight, height])

for i in X:
    rank = 1
    for j in X:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    
    print(rank, end = ' ')

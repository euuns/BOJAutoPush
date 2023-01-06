l, p = map(int, input().split())
n = list(map(int, input().split()))
for i in range(len(n)):
    print(n[i]-(l*p), end=' ')
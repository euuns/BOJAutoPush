from collections import deque

n, k = map(int,input().split())
num = deque([]) ; result = []
for i in range(n):
    num.append(i+1)

while num:
    for i in range(k-1):
        num.append(num.popleft())
    result.append(num.popleft())

print('<', end='')
for i in range(len(result)):
    if i < len(result)-1:
        print(result[i], end=", ")
    else:
        print(result[i], end='')
print('>')
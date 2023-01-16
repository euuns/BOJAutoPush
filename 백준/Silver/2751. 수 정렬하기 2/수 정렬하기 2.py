import sys

n = int(input())
a = []
for i in range(n):
    a.append(int(sys.stdin.readline()))

for i in sorted(a):
    sys.stdout.write(str(i)+'\n')
from collections import deque
import sys

n = deque([ x for x in range(1, int(sys.stdin.readline())+1) ])

while len(n) > 1:
    n.popleft()
    n.append(n.popleft())

print(n[0])
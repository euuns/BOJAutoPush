import sys
import math
N = list(map(int, sys.stdin.readline().strip()))

room = [0]*10

for i in N:
    cnt = 1
    if room[i] >= cnt:
        cnt = room[i] + 1
    room[i] = cnt

room[6] = math.ceil((room[6] + room[9]) / 2)
room.remove(room[9])

print(max(room))
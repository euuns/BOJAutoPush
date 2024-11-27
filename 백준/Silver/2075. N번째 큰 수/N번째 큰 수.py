import sys
import heapq

N = int(sys.stdin.readline())
heap_List = []

heap_List = list(map(int, input().split()))
heapq.heapify(heap_List)

for i in range(N-1):
    n_list = list(map(int, input().split()))
    
    for n in n_list:
        if heap_List[0] < n:
            heapq.heappop(heap_List)
            heapq.heappush(heap_List, n)

print(heap_List[0])
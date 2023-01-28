import sys

def search(arr,value):
    start = 0
    end = n-1
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == value:
            return True
        elif arr[mid] > value:
            end = mid-1
        else:
            start = mid+1

for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    n_list = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    m_list = list(map(int, sys.stdin.readline().split()))

    n_list.sort()
        
    for i in m_list:
        if search(n_list, i):
            print('1')
        else:
            print('0')
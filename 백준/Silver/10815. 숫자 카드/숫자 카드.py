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

n = int(input())
A = list(map(int, input().split()))
A.sort()

m = int(input())
target_list = list(map(int, input().split()))

for i in range(m):
    if search(A,target_list[i]):
        print('1', end=' ')
    else:
        print('0', end=' ')
def search(arr, value):
    start = 0
    end = n-1

    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == value:
            return True
        elif arr[mid] > value:
            end = mid-1
        elif arr[mid] < value:
            start = mid+1


n = int(input())
A = list(map(int, input().split()))
m = int(input())
mList = list(map(int, input().split()))

A.sort()
for i in range(m):
    if search(A,mList[i]):
        print(1)
    else:
        print(0)
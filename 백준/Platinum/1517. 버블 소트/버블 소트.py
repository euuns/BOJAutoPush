n = int(input())
li = list(map(int, input().split()))
cnt = 0

def merge(start, end):
    global cnt, li
    resultList = []

    #분할
    if start < end:
        mid = (start+end) // 2
        merge(start,mid)
        merge(mid+1,end)

        left, right = start, mid+1

        #병합
        while left<=mid and right<=end:
            if li[left] <= li[right]:
                resultList.append(li[left])
                left += 1
            else:
                resultList.append(li[right])
                right += 1
                cnt += (mid - left +1)
        
        if left <= mid:
            resultList = resultList + li[left:mid+1]
        if right <= end:
            resultList = resultList + li[right:end+1]

        for i in range(len(resultList)):
            li[start+i] = resultList[i]


merge(0, n-1)
print(cnt)
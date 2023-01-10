n = int(input())
li = sorted(list(map(int, input().split())))

start = 0
end = n-1
temp = abs( li[start] + li[end] )

left, right = start, end

while start < end:
    if li[start]+li[end] == 0:
        left = start
        right = end
        break
    if temp > abs(li[start]+li[end]):
        temp = abs(li[start]+li[end])
        left = start
        right = end
    elif 0 < li[start]+li[end]:
        end -= 1
    elif 0 > li[start]+li[end]:
        start += 1

print(li[left],li[right])
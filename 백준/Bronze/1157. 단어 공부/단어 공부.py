a = list(input().upper())
a_set = sorted(list(set(a)))
cnt = []

for i in a_set:
    cnt.append(a.count(i))

if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(a_set[cnt.index(max(cnt))])
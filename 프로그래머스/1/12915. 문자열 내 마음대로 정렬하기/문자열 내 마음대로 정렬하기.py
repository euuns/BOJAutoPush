def solution(strings, n):
    strings.sort()
    sort_str = sorted(strings, key=lambda x:x[n])
    
    return sort_str
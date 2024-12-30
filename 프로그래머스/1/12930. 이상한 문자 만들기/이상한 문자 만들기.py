def solution(s):
    result = ""
    word = list(map(str, s.split(' ')))

    for i in word:
        n = 0
        for j in i:
            n += 1
            if n%2 == 1:
                result += j.upper()
            else:
                result += j.lower()
    
        result += " "

    return result[:-1]
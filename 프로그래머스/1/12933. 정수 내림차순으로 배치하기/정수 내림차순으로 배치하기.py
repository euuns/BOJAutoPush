def solution(n):
    answer = sorted(str(n), reverse=True)
    return int(''.join(answer))
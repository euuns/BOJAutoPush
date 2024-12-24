def solution(numbers):
    answer = 0
    sum = 0
    for n in numbers:
        sum += n

    answer = sum / len(numbers)
    return answer
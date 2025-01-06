def solution(array, commands):
    answer = []
    for command in commands:
        itoj = sorted(array[command[0]-1:command[1]])
        answer.append(itoj[command[2]-1])
    return answer
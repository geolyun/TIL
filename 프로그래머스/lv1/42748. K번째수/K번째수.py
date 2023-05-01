def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        s = commands[i][0]
        e = commands[i][1]
        num = commands[i][2]
        result = array[s-1:e]
        sorted_result = sorted(result)
        answer.append(sorted_result[num-1])
    print(answer)
    return answer
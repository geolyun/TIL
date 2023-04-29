def solution(strings, n):
    answer = []
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]
    
    sorted_str = sorted(strings)
    for i in range(len(sorted_str)):
        answer.append(sorted_str[i][1:])
    
    print(answer)
    return answer
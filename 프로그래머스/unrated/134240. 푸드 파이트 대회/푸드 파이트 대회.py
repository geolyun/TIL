def solution(food):
    answer = ''
    lf = []
    rf = []
    zero = [0]
    for i in range(1, len(food)):
        for j in range(food[i]//2):
            lf.append(i)
            rf.append(i)
    rf = rf[::-1]
    result = lf + zero + rf
    for i in range(len(result)):
        answer += str(result[i])
    print(answer)
    return answer
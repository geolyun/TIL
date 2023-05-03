def solution(answers):
    answer = []
    score = []
    a1 = [1, 2, 3, 4, 5] * 10000
    a2 = [2, 1, 2, 3, 2, 4, 2, 5] * 10000
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 10000
    a1c = 0
    a2c = 0
    a3c = 0
    
    for j in range(len(answers)):
        if a1[j] == answers[j]:
            a1c += 1
    score.append(a1c)
    
    for j in range(len(answers)):
        if a2[j] == answers[j]:
            a2c += 1
    score.append(a2c)
    
    for j in range(len(answers)):
        if a3[j] == answers[j]:
            a3c += 1
    score.append(a3c)
    
    for i in range(len(score)):
        if max(score) == score[i]:
            answer.append(i+1)
    
    return answer
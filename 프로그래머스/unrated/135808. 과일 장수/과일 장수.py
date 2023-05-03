def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse = True)
    box = [score[i:i+m] for i in range(0, len(score), m)]
    
    for i in range(len(box)):
        if len(box[i]) == m:
            answer += min(box[i]) * m
    
    print(answer)
    return answer
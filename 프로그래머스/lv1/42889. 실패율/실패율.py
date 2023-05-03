def solution(N, stages):
    answer = [] # 분자에 들어갈 수를 입력
    result = [] # 각 스테이지를 클리어하지 못한 전체 인원의 수
    p = [] # 분모에 들어갈 수를 입력
    a = {} # 실패율을 인덱스 값과 함께 입력
    r_answer = [] # 정답 배열
    person = len(stages)
    for i in range(1, N+1):
        mo = 0
        for j in range(len(stages)):
            if i >= stages[j]:
                mo += 1
        result.append(mo)
        
    answer.append(result[0])
    
    for i in range(1, len(result)):
        answer.append(result[i] - result[i-1])
    
    for i in range(len(answer)):
        p.append(person)
        person = person - answer[i]
        if person < 0:
            p.append(0)
            break
    
    for i in range(len(p)):
        if p[i] == 0:
            a[i+1] = 0    
        else:
            a[i+1] = answer[i] / p[i]
        
    a = sorted(a.items(), key=lambda x: (-x[1], x[0]))
    
    for i in range(len(a)):
        r_answer.append(a[i][0])

    return r_answer
def solution(t, p):
    answer = 0
    num = []
    idx = len(p)
    
    for i in range(0, len(t)-idx+1):
        num.append(int(t[i:i+idx]))
        
    for i in range(len(num)):
        if num[i] <= int(p):
            answer += 1
    
    print(answer)
    return answer
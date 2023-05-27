import math

def solution(progresses, speeds):
    answer = []
    cnt = 1
    maxrem = int(math.ceil((100 - progresses[0]) / speeds[0]))
    
    for i in range(1, len(progresses)):
        progresses[i] = 100 - progresses[i]
        rem = int(math.ceil(progresses[i] / speeds[i]))
        
        if rem > maxrem:
            maxrem = rem
            answer.append(cnt)
            cnt = 1
        else:
            cnt += 1
    answer.append(cnt)
    
    return answer
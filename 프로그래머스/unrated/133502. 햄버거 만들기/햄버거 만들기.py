def solution(ingredient):
    answer = 0
    ham = [1,2,3,1]
    s = -1
    
    while s < len(ingredient)-4:
        s += 1
        if ingredient[s:s+4] == ham:
            del ingredient[s:s+4]
            answer += 1
            s = s-3
            
    return answer
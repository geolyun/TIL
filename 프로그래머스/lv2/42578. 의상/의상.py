def solution(clothes):
    answer = 0
    n = len(clothes)
    s = 1
    cloth = {}
    
    for idx, val in clothes:
        if val in cloth:
            cloth[val].append(idx)
        else:
            cloth[val] = [idx]
    
    for i in cloth:
        s *= len(cloth[i]) + 1
    
    answer = s-1
    return answer
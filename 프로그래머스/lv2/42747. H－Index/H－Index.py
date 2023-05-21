def solution(citations):
    answer = 0
    s = -1
    m = max(citations)
    
    while s <= m:
        up = 0
        down = 0
        s += 1
        for i in citations:
            if i >= s:
                up += 1
            else:
                down += 1
        if up >= s:
            answer = s

    return answer
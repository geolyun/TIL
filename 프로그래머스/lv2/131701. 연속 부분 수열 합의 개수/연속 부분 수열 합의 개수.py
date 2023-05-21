def solution(elements):
    answer = 0
    l = []
    n = len(elements)
    elements = elements * 2
    
    for i in range(1, n+1):
        for j in range(n):
            l.append(sum(elements[j:j+i]))
    
    l = list(set(l))
    answer = len(l)
    return answer
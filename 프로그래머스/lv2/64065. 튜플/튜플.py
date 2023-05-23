def solution(s):
    answer = []
    l = []
    h = {}
    srcs = s[2:-2].split('},{')
    
    for src in srcs:
        temp = list(map(int, src.split(',')))
        l.append(temp)
    
    l = sorted(l, key = len)
    answer.append(l[0][0])
    
    for i in range(1, len(l)):
        result = [item for item in l[i] + l[i-1] if item not in l[i] or item not in l[i-1]]
        answer += result
    return answer
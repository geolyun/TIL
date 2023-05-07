def solution(s, skip, index):
    answer = ''
    alp = "abcdefghijklmnopqrstuvwxyz"
    res = []
    
    for i in alp:
        if i in skip:
            alp = alp.replace(i, "")
    
    for i in range(len(s)):
        a = (alp.index(s[i]) + index) % len(alp)
        
        answer += alp[a]
    return answer
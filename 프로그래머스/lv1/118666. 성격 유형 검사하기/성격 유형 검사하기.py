def solution(survey, choices):
    answer = ''
    n = ['R', 'T', 'C', 'F', 'J', 'M', "A", 'N']
    cnt = [0] * 8
    h = len(survey)
    for i in range(h):
        v = list(survey[i])
        v1 = n.index(v[0])
        v2 = n.index(v[1])
        if choices[i] - 4 > 0:
            cnt[v2] += choices[i] - 4
        elif choices[i] - 4 < 0:
             cnt[v1] += 4 - choices[i]
    
    for i in range(0, 8, 2):
        if cnt[i] > cnt[i+1]:
            answer += n[i]
        elif cnt[i] < cnt[i+1]:
            answer += n[i+1]
        else:
            answer += min(n[i], n[i+1])
    return answer
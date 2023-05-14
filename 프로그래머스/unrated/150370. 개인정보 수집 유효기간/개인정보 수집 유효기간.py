def solution(today, terms, privacies):
    answer = []
    t = list(map(int, today.split(".")))
    t_cnt = (t[0]-1) * 12 * 28 + (t[1]-1) * 28 + t[2]
    term = {}
    
    for i in terms:
        key, value = i.split()
        term[key] = int(value)
    
    for i in range(len(privacies)):
        d, l = privacies[i].split()
        dd = list(map(int, d.split(".")))
        d_cnt = (dd[0]-1) * 12 * 28 + (dd[1]-1) * 28 + dd[2]
        v = int(term[l])
        d_cnt += v*28
        
        if t_cnt >= d_cnt:
            answer.append(i+1)

    return answer
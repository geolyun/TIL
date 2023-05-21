def solution(k, tangerine):
    answer = 0
    so = 0
    m = max(tangerine)
    cnt = [0 for i in range(m+1)]
        
    for i in range(len(tangerine)):
        cnt[tangerine[i]] += 1
        
    cnt = sorted(cnt, reverse=True)
    
    for i in cnt:
        if so >= k:
            break
        else:
            so += i
            answer += 1
            
    return answer
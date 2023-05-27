from itertools import permutations

def solution(k, dungeons):
    answer = 0
    all_dungeons = []
    for i in permutations(dungeons,len(dungeons)):
        all_dungeons.append(list(i))
    
    M = 0
    for i in range(len(all_dungeons)):
        cnt = 0
        kk = k
        for j in range(len(all_dungeons[i])):
            m, sleep = all_dungeons[i][j][0], all_dungeons[i][j][1]
            if kk >= m:
                cnt += 1
                kk = kk - sleep
            else:
                break
        if cnt > M:
            M = cnt
            
    answer = M
    return answer
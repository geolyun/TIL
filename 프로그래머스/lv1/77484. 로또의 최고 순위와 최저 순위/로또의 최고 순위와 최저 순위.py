def solution(lottos, win_nums):
    answer = []
    rank = [6, 6, 5, 4, 3, 2, 1]
    cnt = 0
    zero_cnt = 0
    for i in range(len(lottos)):
        for j in range(len(win_nums)):
            if lottos[i] == win_nums[j]:
                cnt += 1
    
    for i in lottos:
        if i == 0:
            zero_cnt += 1
    
    l_cnt = cnt + zero_cnt
    if l_cnt > 6:
        l_cnt = 6
    if cnt < 1:
        cnt = 1
    
    answer.append(rank[l_cnt])
    answer.append(rank[cnt])
    return answer
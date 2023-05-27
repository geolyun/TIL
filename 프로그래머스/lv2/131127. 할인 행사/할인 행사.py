def solution(want, number, discount):
    answer = 0
    cnt = sum(number)
    
    for i in range(len(discount)-cnt+1):
        ord = discount[i:i+cnt]
        cnt_list = []
        for j in want:
            cnt_list.append(ord.count(j))
        if cnt_list == number:
            answer += 1
    return answer
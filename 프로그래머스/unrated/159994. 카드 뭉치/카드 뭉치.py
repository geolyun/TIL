def solution(cards1, cards2, goal):
    answer = ''
    s1 = 0
    s2 = 0
    idx1 = []
    idx2 = []
    
    for i in range(len(goal)):
        if goal[i] == cards1[s1]:
            idx1.append(s1)
            s1 += 1
            if s1 > len(cards1)-1:
                break
                
    for i in range(len(goal)):
        if goal[i] == cards2[s2]:
            idx2.append(s2)
            s2 += 1
            if s2 > len(cards2)-1:
                break
                
    if len(idx1) + len(idx2) == len(goal):
        answer += "Yes"
    else:
        answer += "No"
    return answer
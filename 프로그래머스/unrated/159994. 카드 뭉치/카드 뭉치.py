def solution(cards1, cards2, goal):
    answer = ''
    s1 = 0
    s2 = 0
    idx1 = []
    idx2 = []
    
    # cards1, cards2의 0번 인덱스부터 goal요소에 대조
    # 카드가 순서대로 되어있지 않으면 순서대로 되어있지 않은 인덱스는 값에 추가 x
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
    
    # cards1과 cards2의 카드가 옳게 인덱스를 모은 리스트에 추가되면 그 두 리스트의 길이와 goal 리스트의 길이가 같아야함
    if len(idx1) + len(idx2) == len(goal):
        answer += "Yes"
    else:
        answer += "No"
    return answer
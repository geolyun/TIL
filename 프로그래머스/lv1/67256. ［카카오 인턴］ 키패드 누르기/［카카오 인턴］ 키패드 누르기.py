def solution(numbers, hand):
    answer = ''
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*':[3, 0], 0: [3, 1], '#': [3, 2]}
    
    l = dic["*"]
    r = dic["#"]
    
    for i in numbers:
        idx = dic[i]
        if i in [1, 4, 7]:
            answer += "L"
            l = idx
        elif i in [3, 6, 9]:
            answer += "R"
            r = idx
        else:
            if abs(l[0]-idx[0]) + abs(l[1]-idx[1]) < abs(r[0]-idx[0]) + abs(r[1]-idx[1]):
                answer += "L"
                l = idx
            elif abs(l[0]-idx[0]) + abs(l[1]-idx[1]) > abs(r[0]-idx[0]) + abs(r[1]-idx[1]):
                answer += "R"
                r = idx
            else:
                if hand == "right":
                    answer += "R"
                    r = idx
                else:
                    answer += "L"
                    l = idx

    return answer
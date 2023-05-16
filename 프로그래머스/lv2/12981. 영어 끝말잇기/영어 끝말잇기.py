def solution(n, words):
    answer = []
    word_list = []
    fail = 0
    
    word_list.append(words[0])
    for i in range(1, len(words)):
        if words[i-1][-1] == words[i][0]:
            if words[i] not in word_list:
                word_list.append(words[i])
            else:
                fail = i+1
                break
        else:
            fail = i+1
            break
    
    if fail == 0:
        num, order = 0, 0
    else:
        if fail % n == 0:
            num = n
            order = fail // n
        else:
            num = fail % n
            order = (fail // n) + 1
            
    answer = [num, order]
    return answer
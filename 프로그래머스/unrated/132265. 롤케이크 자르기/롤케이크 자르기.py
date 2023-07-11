from collections import Counter

def solution(topping):
    answer = 0
    bro = Counter(topping)
    me = set()
    
    for i in topping:
        bro[i] -= 1
        if bro[i] == 0:
            del bro[i]
        me.add(i)
        if len(bro) == len(me):
            answer += 1
    
    return answer
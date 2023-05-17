def solution(people, limit):
    answer = 0
    cnt = 0
    s = 0
    e = len(people) - 1
    people = sorted(people, reverse = True)
    
    while s <= e:
        if people[s] + people[e] > limit:
            cnt += 1
            s += 1
        else:
            cnt += 1
            s += 1
            e -= 1
    answer = cnt
    return answer
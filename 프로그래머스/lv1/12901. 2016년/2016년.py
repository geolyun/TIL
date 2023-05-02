def solution(a, b):
    answer = ''
    All = 0
    cnt = 1
    s = 5
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    for i in range(a-1):
        All += day[i]
    All += b
    while All > cnt:
        s += 1
        cnt += 1
        if s > len(week)-1:
            s = 0
    answer = week[s]
    return answer
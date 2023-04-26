def solution(s):
    answer = ''
    s = list(s)
    index = 0
    for i in range(len(s)):
        if s[i] == " ":
            answer += s[i]
            index = 0
        elif index % 2 == 0:
            s[i] = s[i].upper()
            answer += s[i]
            index += 1
        else:
            s[i] = s[i].lower()
            answer += s[i].lower()
            index += 1
    return answer
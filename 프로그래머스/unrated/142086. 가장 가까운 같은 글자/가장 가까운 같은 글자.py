def solution(s):
    answer = [-1]
    for i in range(1, len(s)):
        cnt = 0
        for j in range(i-1, -1, -1):
            if s[i] == s[j]:
                answer.append(i-j)
                cnt += 1
                break
        if cnt == 0:
            answer.append(-1)
    print(answer)
    return answer
def solution(n):
    answer = []
    n = str(n)
    for i in n:
        answer.append(int(i))
    answer = answer[::-1]
    print(answer)
    return answer
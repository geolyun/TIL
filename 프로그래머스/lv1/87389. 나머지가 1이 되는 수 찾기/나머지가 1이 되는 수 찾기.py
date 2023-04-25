def solution(n):
    result = []
    for i in range(1, n+1):
        if n % i == 1:
            result.append(i)
    answer = result[0]
    return answer
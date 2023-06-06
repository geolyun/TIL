def solution(n):
    answer = 0
    num1 = 1
    num2 = 2
    for i in range(3, n+1):
        answer = num1 + num2
        num1 = num2
        num2 = answer
    answer = answer % 1000000007
    return answer
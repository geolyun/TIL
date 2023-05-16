def solution(n):
    answer = 0
    Fib = [0, 1]
    
    for i in range(2, 100001):
        Fib.append(Fib[i-2] + Fib[i-1])
    
    answer = Fib[n] % 1234567
    return answer
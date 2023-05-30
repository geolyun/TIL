def solution(n, k):
    answer = 0
    
    if n == 0:
        return '0'

    result = []
    while n > 0:
        remainder = n % k
        n = n // k
        result.append(remainder)

    num = ''.join(str(i) for i in result[::-1])
    
    num_l = list(num.split("0"))
    
    P = []
    for element in num_l:
        if element.isdigit():
            P.append(int(element))
    
    def Isprime(x):
        if x == 1:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True
    
    for i in P:
        if Isprime(i) == True:
            answer += 1
    return answer
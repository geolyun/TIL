n = int(input())
num = list(map(int, input().split()))

def reverse(x):
    rev = (str(x)[::-1])
    return int(rev)

def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
        
for i in num:
    a = reverse(i)
    if isPrime(a) == True:
        print(a, end=' ')
    else:
        continue
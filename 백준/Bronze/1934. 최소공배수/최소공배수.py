T = int(input())

for i in range(T):
    M = 0
    A, B = map(int, input().split())
    m = min(A, B)
    for i in range(1, m+1):
        if A % i == 0 and B % i == 0:
            M = i
    print((A*B)//M)
    
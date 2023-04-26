def factorial(x):
    n = 1
    for i in range(1, x+1):
        n = n*i
    return n

N = int(input())
N = factorial(N)
N = list(str(N))
cnt = 0

for i in range(len(N)):
    if N[-1] == "0":
        N.pop(-1)
        cnt += 1
    else:
        break

print(cnt)
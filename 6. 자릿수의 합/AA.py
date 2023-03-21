N = int(input())
num = list(map(int, input().split()))

def digit_sum(x):
    a = [int(i) for i in str(x)]
    return sum(a)

max = 0

for i in num:
    tot = digit_sum(i)
    if tot>max:
        max = tot
        res = i

print(res)



# for문이 도는 동안 무엇이 변하는지 알아야함
n, m = map(int, input().split())

num = list(map(int, input().split()))

def quick_sort(num):
    if len(num) <= 1:
        return num
    p = len(num) // 2
    front, pivot, back = [], [], []

    for i in num:
        if i < num[p]:
            front.append(i)
        elif i > num[p]:
            back.append(i)
        else:
            pivot.append(i)
    return quick_sort(front) + quick_sort(pivot) + quick_sort(back)

result = quick_sort(num)

for i in range(n):
    if result[i] == m:
        print(i+1)
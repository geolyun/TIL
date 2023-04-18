n = int(input())

num = list(map(int, input().split()))

sorted_num = set(num)
sorted_num2 = sorted(sorted_num)

result = {sorted_num2[i] : i for i in range(len(sorted_num2))}

for i in num:
    print(result.get(i), end = ' ')
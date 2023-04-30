A, B = map(int, input().split())
m = int(input())
num = list(map(int, input().split()))

result = 0

num = num[::-1]

for i in range(len(num)):
    result += num[i] * (A ** i)

B_result = []
while result // B:
    B_result.append(result % B)
    result = result // B
B_result.append(result)

for i in range(len(B_result)-1, -1, -1):
    print(B_result[i], end=" ")
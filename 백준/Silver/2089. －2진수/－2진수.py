n = int(input())

stack = []

while n != 0:
    if n % -2 != 0:
        stack.append(abs(n % -2))
        n = (n // -2) + 1       
    else:
        stack.append(n%-2)
        n = n//-2

stack = stack[::-1]

if len(stack) == 0:
    stack.append(0)

for i in range(len(stack)):
    print(stack[i], end='')
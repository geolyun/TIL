S = input()

result = []

for i in S:
    n = ord(i)
    if "a" <= i <= "z":
        n += 13
        if n > 122:
            n -= 26
    elif "A" <= i <= "Z":
        n += 13
        if n > 90:
            n -= 26       
    result.append(chr(n))

for i in result:
    print(i, end='')    
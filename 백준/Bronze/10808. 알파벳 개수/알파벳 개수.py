S = input()

alp = [0] * 26

for i in S:
    n = ord(i) - ord("a")
    alp[n] += 1

for i in alp:
    print(i, end = " ")
S = input()

jup = []

for i in range(len(S)):
    jup.append(S[i:])

sorted_jup = sorted(jup)

for i in sorted_jup:
    print(i)
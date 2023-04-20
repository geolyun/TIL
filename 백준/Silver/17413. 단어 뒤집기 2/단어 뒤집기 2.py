import sys
s = list(sys.stdin.readline().rstrip())

i = 0
start = 0

while i < len(s):
    if s[i] == "<":
        i += 1
        while s[i] != ">":
            i += 1
        i += 1
    elif s[i].isalnum():
        start = i
        while i < len(s) and s[i].isalnum():
            i += 1
        result = s[start:i]
        result.reverse()
        s[start:i] = result
    else:
        i += 1

print("".join(s))
def solution(n):
    answer = 0
    a = n
    n = bin(n)
    n = n[2:]
    cnt = n.count("1")
    while True:
        a += 1
        if bin(a).count("1") == cnt:
            answer = a
            break
    print(answer)
    return answer
while 1:
    try:
        res = [0] * 4
        N = str(input())

        for j in N:
            if "a" <= j <= "z":
                res[0] += 1
            elif "A" <= j <= "Z":
                res[1] += 1
            elif j == " ":
                res[3] += 1
            else:
                res[2] += 1
        
        print(*res)

    except EOFError:
        break
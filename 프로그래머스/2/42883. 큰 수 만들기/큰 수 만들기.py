def solution(number, k):
    answer = []
    l = len(number) - k
    start = 0    
    
    while l > 0:
        Max = "0"
        if (-l+1) == 0:
            check = number[start:]
        else:
            check = number[start:-l+1]
        for i in check:
            if i > Max:
                Max = i
                if Max == "9":
                    break
        answer.append(Max)
        idx = check.index(Max)
        start += idx + 1
        l -= 1
        
    result = "".join(answer)
    return result
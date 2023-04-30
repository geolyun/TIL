def solution(s):
    code = []
    answer = ""
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    alp = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    a = ""
    
    for i in s:
        if i.isalpha():
            a += i
        else:
            code.append(int(i))
        for j in range(len(alp)):
            if a == alp[j]:
                code.append(num[j])
                a = ""
            
    for i in range(len(code)):
        answer += str(code[i])
    answer = int(answer)
    return answer
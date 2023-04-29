def solution(n, arr1, arr2):
    code = [[] for i in range(n)]
    answer = []
    for i in range(n):
        arr1[i] = bin(arr1[i])[2:]
        arr1[i] = arr1[i].zfill(n)
        
        arr2[i] = bin(arr2[i])[2:]
        arr2[i] = arr2[i].zfill(n)

    for i in range(n):
        for j in range(n):
            if arr1[i][j] == "0" and arr2[i][j] == "0":
                code[i].append(" ")
            else:
                code[i].append("#")
                
    for i in range(n):
        answer.append(''.join(code[i]))

    print(answer)
    return answer
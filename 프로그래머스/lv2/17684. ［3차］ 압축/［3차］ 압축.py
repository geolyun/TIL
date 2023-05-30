def solution(msg):
    answer = []
    word = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    
    i = 0
    s = msg[0]
    while i != len(msg):
        if s in word:
            if i != len(msg)-1:
                i += 1
            else:
                answer.append(word.index(s)+1)
                break
            s += msg[i]
        else:
            answer.append(word.index(s[:len(s)-1]) + 1)
            word.append(s)
            s = msg[i]
    
    print(answer)
    return answer
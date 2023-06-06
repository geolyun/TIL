def solution(word):
    answer = 0
    alp = ["A", "E", "I", "O", "U"]
    l = [781, 156, 31, 6, 1]
    
    for i in range(len(word)):
        answer += alp.index(word[i]) * l[i]
    answer += len(word)
    return answer
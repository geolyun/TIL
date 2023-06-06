def solution(skill, skill_trees):
    answer = 0
    arr = []
    
    for i in range(len(skill)):
        arr.append(skill[0:i+1])
    
    for i in skill_trees:
        tree = ""
        for j in i:
            if j in skill:
                tree += j
        if tree in arr or len(tree) == 0:
            answer += 1
    print(arr)
    return answer
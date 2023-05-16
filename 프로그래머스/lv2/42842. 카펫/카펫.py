def solution(brown, yellow):
    answer = []
    car = brown + yellow

    for i in range(3, car+1):
        if car % i == 0:
            a, b = i, car // i
            
            if (a-2) * (b-2) == yellow:
                answer = [a, b]
    
    print(answer)
    return answer
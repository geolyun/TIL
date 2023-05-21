import math

def solution(n,a,b):
    answer = 0
    cnt = 0
    
    while a != b:
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        cnt += 1
    
    answer = cnt
    return answer
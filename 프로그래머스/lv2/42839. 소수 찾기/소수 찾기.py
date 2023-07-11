def isPrime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int((x**0.5) + 1)):
        if x%i == 0:
            return False
    return True

# dfs로 만들 수 있는 모든 숫자들을 탐색
# 재귀를 이용
def search_number(numbers, i, check_prime, num_list):
    for j in numbers:
        new_num = i + j
        r = numbers.replace(j, "", 1)
        if int(new_num) not in num_list:
            num_list.append(int(new_num))
            if isPrime(int(new_num)) == True:
                check_prime.append(int(new_num))
        if r:
            search_number(r, new_num, check_prime, num_list)
        
def solution(numbers):
    check_prime = []
    num_list = []
    answer = 0
    
    for i in numbers:
        r = numbers.replace(i, "", 1)
        if int(i) not in num_list:
            num_list.append(int(i))
            if isPrime(int(i)) == True:
                check_prime.append(int(i))
        search_number(r, i, check_prime, num_list)    
    
    answer = len(check_prime)
    return answer
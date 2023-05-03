def solution(nums):
    answer = 0
    sum = []
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                sum.append(nums[i]+nums[j]+nums[k])
    
    
    for i in range(len(sum)):
        n = sum[i]
        prime = True
        for j in range(2, n):
            if n % j == 0:
                prime = False
                break
        if prime == True:
            answer += 1

    return answer
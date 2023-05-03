def solution(nums):
    answer = 0
    p = len(nums) // 2
    nums = list(set(nums))
    
    if len(nums) <= p:
        answer = len(nums)
    else:
        answer = p
    return answer
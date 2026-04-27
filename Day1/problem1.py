# Problem 1: Two Sum (Classic)

# Question:
# Given an array nums and an integer target, return indices of two numbers such that they add up to target.  


def two_sum(nums, target):
    seen = {}
    
    for i in range(len(nums)):
        complement = target - nums[i]
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[nums[i]] = i
nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))

# Problem 2: Contains Duplicate

# Question:
# Given an array, return True if any value appears at least twice, otherwise False.


def contains_duplicate(nums):
    seen = set()
    
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    
    return False
        
        
arr = [1,2,3,4,4]
print(Contains_Duplicate(arr))
            
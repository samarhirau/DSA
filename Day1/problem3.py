# Problem 3: Maximum Subarray

def max_subarray(nums):
    current_sum = nums[0]
    max_sum = nums[0]
    
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum


# arr = [-2,1,-3,4,-1,2,1,-5,4]
# print(max_subarray(arr))

# Kadane’s Algorithm (Optimal Solution)

def max_subarray(nums):
    current_sum = nums[0]
    max_sum = nums[0]
    start = end = temp_start = 0
    
    for i in range(1, len(nums)):
        if current_sum < 0:
            current_sum = nums[i]
            temp_start = i
        else:
            current_sum += nums[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    
    return nums[start:end+1]
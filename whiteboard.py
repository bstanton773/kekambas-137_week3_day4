# Running Sum of 1d Array
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
# Example 3:
# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]


# Out of Place
def solution(nums):
    running_sum = 0
    output = []
    for num in nums:
        running_sum += num
        output.append(running_sum)
    return output

# In-Place
def solution(nums):
    running_sum = 0
    for i in range(len(nums)):
        running_sum += nums[i]
        nums[i] = running_sum
    return nums

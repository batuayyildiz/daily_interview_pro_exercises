# Daily Interview Pro Question
# Find a unique number in the list.

def singleNumber(nums):
  # Fill this in.
  size = len(nums)
  
  for i in range(size):
  	if nums.count(nums[i]) == 1 :
  		return i

print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
# 1



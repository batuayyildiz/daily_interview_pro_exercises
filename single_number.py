# def singleNumber(nums):
#   # Fill this in.
#   size = len(nums)
  
#   for i in range(size):
#   	if nums.count(nums[i]) == 1 :
#   		return i

# print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
# # 1


arr = list(map(int, input().split()))

print(f"Sayı 1: {arr[0]}")
print(f"Sayı 2: {arr[1]}")

x = [int(x) for x in input().split()] 
print("Number of list is: ", x)  

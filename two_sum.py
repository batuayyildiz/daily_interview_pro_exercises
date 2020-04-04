# Daily Interview Pro Question
# You're given a list and target value.
# Return whether or not there are two numbers in the list that add up to target.

def two_sum(my_list, target):

	size = len(my_list)

	for i in range(size):
		element = my_list.pop(i)
		#print(my_list)
		new_size = len(my_list)
		for j in range(new_size):
			if((my_list[j] + element) == target):
				return True
		my_list.insert(i, element) # Elemanı kaybetmemek için dış döngü bitmeden tekrar aynı pozisyona eklenmeli.
	return False


# my_list = [4,7,1,-3,2]

# print(two_sum(my_list, 5)) # True


# my_list = [3,7,-5,4,13,1,4]
# target = -4

# print(two_sum(my_list, target)) # True


my_list = [1,2,3,4,5]
target = 10
print(two_sum(my_list, target)) # False
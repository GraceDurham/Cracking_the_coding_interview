

def is_unique(str):
	""" Write a function that checks to see if a string has duplicates,
		using other data structures"""

	if len(str) > 128:
		return False

	char_set = [False for _ in range(128)]
	for char in str:
		val = ord(char)
		if char_set[val]:
			#Char already found in string
			return False
		char_set[val] = True

	return True


print(is_unique("grace"))



def no_duplicates(my_string):
	""" Write a function that checks to see if a string has duplicates,
		using other data structures"""
    
	test_set = set(my_string)
        
    
	if len(test_set) == len(my_string):
		return "Your string '{}' has all unique chars".format(my_string)
 
	return "Your string '{}' has duplucate chars".format(my_string)
    
    
    
test_string_1 = "timothy"

test_string_2 = "grace"


print(no_duplicates(test_string_1))
print(no_duplicates(test_string_2))



def is_unique(test_string):
	""" Write a function that checks to see if a string has duplicates,
		without using other data structures"""

	test_str = len(test_string)

	for i in range(test_str):
		sliced_front_string = test_string[i: i+1] # Capture first index of string via slicing
		sliced_back_string = test_string[i+1 :test_str] # Capture second half of string less the first index via slicing


		if sliced_front_string in sliced_back_string: # fail fast no need for iteration to check next index against next sub string found duplicate
			return "Sorry '{}' string does not have all unique characters.".format(test_string)


		else:
			for i in range(len(sliced_back_string)):
				sliced_front_string = test_string[i+1: i+2] # increment string slicing starting at index 1
				sliced_back_string = test_string[i+2: test_str] # increment string slicing starting at index 2


				if sliced_front_string in sliced_back_string: # check for membership of substring slices after incrementing 
					return "Sorry '{}' string does not have all unique characters.".format(test_string)

		return "Yay '{}' string has all unique characters.".format(test_string) # After checking each sliced index with second half sliced index return string is unique did not find duplicates


grace = "grace"
timothy = "timothy"
matty = "matty"

print(is_unique(grace))
print(is_unique(timothy))
print(is_unique(matty))



def is_unique_too(test_string):

	test_str = set(test_string)

	if len(test_string) == len(test_str):
		return True
	return False

timothy = "timothy"
grace = "grace"
print(is_unique_too(grace))
print(is_unique_too(timothy))
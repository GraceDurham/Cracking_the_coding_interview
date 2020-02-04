


def sort_strings(check_str):
	"""Sort strings to put in the same order to check if permutation"""


	checked_str = check_str.lower().strip() # make string lower case and strip white space

	checked_strs = sorted(checked_str)

	print(checked_strs)

	words = " ".join(checked_strs)

	return words


str_one = sort_strings("God  ")
print(str_one)
str_two = sort_strings("dog")
print(str_two)

str_three = sort_strings(" Grace")
print(str_three)



def boolean_permutation(str_one, str_two):
	"""Compare length of sorted string one and string two to see if permutation of each other"""

	if len(str_one) != len(str_two): # if length of strings not equal then not permutations
		return False
	return True

print(boolean_permutation(str_one, str_two))
print(boolean_permutation(str_one, str_three))


def check_permutation(str_one, str_two):


	n1 = len(str_one)
	n2 = len(str_two)

	if n1 != n2:  # Fail fast permutations should be the same length
		return False

	dict_ascii = {}

	for i in range(129):
		dict_ascii[i] = 0
	# print(list_ascii)


	for i in range(n1):
		if ord(str_one[i]) in dict_ascii:
			print(ord(str_one[i]))
			dict_ascii[ord(str_one[i])] = dict_ascii[ord(str_one[i])] + 1
	print(dict_ascii)  # find ordinal value and increment value by one if ordinal value in dictionary


	for i in range(n2):
		if ord(str_two[i]) in dict_ascii: # find ordinal value
			print(ord(str_two[i]))
			dict_ascii[ord(str_one[i])] = dict_ascii[ord(str_one[i])] - 1
			if all(x < 0 for x in dict_ascii.values()): # decrement value by one 
				return False							# if ordinal value in dictionary


	return True

		# if all values are zero than the two strings are permutations


print(check_permutation("grace", "raceg"))
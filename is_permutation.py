


def is_permutation(s1, s2):
	""" Checks if two strings are permutations of each other"""

	n1 = len(s1)
	n2 = len(s2)

	# If the length of both strings is not the same,
	# then they can not be Permutation
	if (n1 != n2):
		False

	# Sort both strings
	s1_sorted = sorted(s1)
	s1 = " ".join(s1_sorted)
	s2_sorted = sorted(s2)
	s2 = " ".join(s2_sorted)

	print(s1)
	print(s2)

	# Compare sorted strings index by index
	for i in range(0, n1, 1):
		if (s1_sorted[i] != s2_sorted[i]):
			return False
	return True

print(is_permutation("dog", "god"))



def one_away(w1, w2):
	"""Given two strings, are they, at most, one edit away?"""

	# Strings length can only vary by, at most, one letter fail fast if more than 1
	if abs(len(w1) - len(w2)) > 1:
		return False


	# Make sure w2 is the shorter string
	if len(w2) > len(w1):
		w1, w2 = w2, w1
		print(w1), print(w2)


	# Keep track of number of wrong letters
	wrong = 0


	# Loop over w1 with i and over w2 with j
	i = j = 0

	while j < len(w2): # stop incrementing when reach length of shorter w2 word

		if w1[i] != w2[j]:

			# We found a wrong letter
			wrong = wrong + 1
			if wrong > 1:
				return False


			# We'll move to the next char in the longer string.
			i = i + 1

			# If same length, move to the next char in shorter string.
			# Otherwise, don't move in shorter string --- this
			# will cover the case of a added letter.
			if len(w1) == len(w2):
				j = j + 1

		else:
			# Both letters match; move to next letter in both
			i = i + 1
			j = j + 1

	return True



print(one_away("pale", "ple"))
print(one_away("pales", "pale"))
print(one_away("pale", "bale"))
print(one_away("pale", "bake"))






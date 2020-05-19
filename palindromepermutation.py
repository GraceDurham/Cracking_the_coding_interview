
def palindrome_permutation(word):
	"""Is the word an anagram of a palindrome?"""

	seen = {}


	word = word.replace(' ', '').lower()
	print(word)

	# Create dictionary letter is the key and count each letter is the value

	for letter in word:
		if letter not in seen:
			seen[letter] = 1
		else:
			seen[letter] = seen[letter] + 1


	# Its a palindrome if the number of odd-counts is either 0 or 1


	seen_an_odd = False


	for count in seen.values(): # Returns a list of values which is the count in the dictionary
		if count % 2 != 0: #letter count is odd
			if seen_an_odd: # seen odd letter count is true count is more than 1 not a palindrome
				return False
			seen_an_odd = True # odd count is 1 or less than is a palindrome

	return True


print(palindrome_permutation("Tact Coa"))
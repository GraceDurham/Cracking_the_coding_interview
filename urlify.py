

1.3 

# Write a method to replace of spaces in a string with '%20'. You may assume that the string 
# has sufficient space at the end to hold the additional characters, and that
# you are given the "true" length of the string. (Note: If implementing in Java, please
# use a character array so that you can perform the operation in place.)


def count_spaces(str):
	""" Returns count of number of white spaces in a string"""

	str = str.strip() # Strips trailing white space not needed to replace with %20

	count = 0

	for string in str:
		if string == " ":
			count = count + 1

	return count

count = count_spaces("Mr John Smith  ")


def urlify(str, count):
	""" Replaces white spaces with %20 """

	replacedstring = str.replace(' ', '%20', count)

	return replacedstring


print(urlify("Mr John Smith    ", count))









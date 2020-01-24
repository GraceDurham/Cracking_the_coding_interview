


def is_unique(str):

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
    
    test_set = set(my_string)
        
    
    if len(test_set) == len(my_string):
        return "Your string '{}' has all unique chars".format(my_string)
    
    return "Your string '{}' has duplucate chars".format(my_string)
    
    
    
test_string_1 = "dardar"

test_string_2 = "simone1234"


print(no_duplicates(test_string_1))
print(no_duplicates(test_string_2))
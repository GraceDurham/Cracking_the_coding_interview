

def is_permutation(s1, s2):
    """ Checks if two strings are permutations of each other"""


    # If the length of both strings is not the same,
    # then they can not be Permutation
    if (len(s1) != len(s2)):
        return False

    # Sort both strings
    s1_sorted = " ".join(sorted(s1))
    s2_sorted = " ".join(sorted(s2))


    # Compare sorted strings index by index
    for i in range(0, len(s1), 1):
        if (s1_sorted[i] != s2_sorted[i]):
            return False
    return True

print(is_permutation("dog", "gdd"))



def is_permu_2(str_1, str_2):
	 """ Checks if two strings are permutations of each other"""

    if str_1 == str_2:
        return "Yay, we have permitation with string '{}'' and '{}'.".format(str_1, str_2)

    else:

        str_1_sorted = "".join(sorted(str_1))
        str_2_sorted = "".join(sorted(str_2))

        if str_1_sorted != str_2_sorted:
            return "Sooo sorry, we do not have permitation with string '{}'' and '{}'.".format(str_1,str_2)
        return "Yay, we have permitation with string '{}'' and '{}'.".format(str_1, str_2)
        

print(is_permu_2("dog", "god"))


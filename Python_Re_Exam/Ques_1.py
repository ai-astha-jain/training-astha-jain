def check_anagrams(valid_string1,valid_string2):
    if len(valid_string1) == len(valid_string2):
        for i in valid_string1:
            if i in valid_string2:
                pass
        print("True")        
    else:
        print("Please take the same length of string input.")


string1 = input("Enter the string: ")
valid_string1 = string1.lower()
print("The string is:", valid_string1)
string2 = input("Enter the another string to check anagrams: ")
valid_string2 = string2.lower()
print("The another string to check anagrams is:", valid_string2)
check_anagrams(valid_string1,valid_string2)


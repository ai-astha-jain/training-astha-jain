def is_valid_string(s):
    if not (s[0].islower() and s[0] not in 'aeiou'):
        return False
    
    if not s.isalpha():
        return False
    
    return True

def extract_strings(string_list):
    return list(filter(is_valid_string, string_list))

input_string = input("Enter a list of strings (separated by spaces): ")
string_list = input_string.split()
result = extract_strings(string_list)
print("Valid strings:", result)




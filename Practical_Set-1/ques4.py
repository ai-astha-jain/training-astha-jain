def is_valid_string(s):
    if not s[0].islower() or s[0] in 'aeiou':
        return False

    for char in s:
        if not char.isalpha():
            return False

    return True

def extract_strings(string_list):
    valid_strings = []
    for s in string_list:
        if is_valid_string(s):
            valid_strings.append(s)
    return valid_strings

string_list = ['Biscuit', 'okhama', 'hello', 'go123', 'check', 'valid', 'game']
result = extract_strings(string_list)
print(result)

def is_valid_number(n):
    if not (1000 <= n <= 9999):
        return False
        
    second_digit = (n // 100) % 10  # Extract the second digit
    last_digit = n % 10  # Extract the last digit
    
    if second_digit % 2 == 0 or last_digit % 2 != 0:
        return False
        
    if n % 3 != 0 and n % 7 != 0:
        return False
    
    return True

def extract_numbers(number_list):
    valid_numbers = [n for n in number_list if is_valid_number(n)]
    return valid_numbers

number_list = list(map(int, input("Enter a list of numbers separated by space: ").split()))
result = extract_numbers(number_list)
print("Valid numbers:", result)


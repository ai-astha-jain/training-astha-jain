def is_valid_number(num):
    if not (1000 <= num <= 9999):
        return False
    
    second_digit = (num // 100) % 10  
    last_digit = num % 10  
    
    if second_digit % 2 == 0 or last_digit % 2 != 0:
        return False

    if num % 8 != 0 and num % 5 != 0:
        return False
    
    return True

def extract_numbers(list_of_numbers):
    valid_numbers = [num for num in list_of_numbers if is_valid_number(num)]
    return valid_numbers

number_list = list(map(int, input("Enter a list of numbers separated by space: ").split()))
result = extract_numbers(number_list)
print("Valid numbers:", result)


def is_valid_number(num,target):
    if not (1 <= num <= 10 ** 4):
        return False
    if not ((-10) ** 9 <= target <= 10 ** 9):
        return False
    return True
    
def output_indices(list_of_numbers,target):
    for i in list_of_numbers:
        for j in list_of_numbers:
            if list_of_numbers[i]+list_of_numbers[j] == target:
                print("The indices are: ",list(num[i],num[j]))
    return output_indices
    
global list2 
def extract_numbers(list_of_numbers):
    list2 = [(num1,num2) for num1 in list_of_numbers for num2 in list_of_numbers if num1 + num2 == target]
    return list2


list_of_numbers = []
target = int(input("Enter the target: "))
no_of_elements = int(input("Enter the no of elements: "))
for i in range(no_of_elements):
    number = int(input("Enter the number"))
    list_of_numbers.append(number)
    i += 1

result = extract_numbers(list_of_numbers)

print("The list of the numbers of which the sum is equal to target is: ",result)

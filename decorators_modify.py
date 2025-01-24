import time 
def decorator(input_num):

    global start_time_code
    start_time_code = time.time()
    #print("The time when code is started : ", start_time_code)
    
    while True:
        print("\n To calculate :\n")
        print(" 1. ADD\n 2. SUBTRACT\n 3. MULTIPLY\n 4. DIVIDE \n 0. EXIT")
        choice = input("Enter the operation choice you want to perform(1/2/3/4/0): ")
        if choice.isdigit():
            choice = int(choice)
        else:
            print("Invalid choice. Please enter the valid choice")
            continue
        num1 = input_num()
        num2 = input_num()
        if choice == 1:
            print("The addition is: ", f"{num1} + {num2} = {num1 + num2}")
        elif choice == 2:
            print("The subtraction is: ", f"{num1} - {num2} = {num1 - num2}")
        elif choice == 3:
            print("The multiply is: ", f"{num1} * {num2} = {num1 * num2}")
        elif choice == 4:
            try:
                print("The division is: ", f"{num1} / {num2} = {num1 / num2}")
            except ZeroDivisionError:
                print("Invalid input.Please enetr valid input.")
        else:
            break
       
@decorator	   
def input_num(): 
    while True:
        try:
            num1 = int(input("Enter the number: "))
            if isinstance(num1, (int,float)):
                return num1
            else:
                print("Please enter the valid integers.")
                continue
        except (NameError, ValueError):
            print("Invalid input. please enter the integers")
            continue

global end_time_code
end_time_code = time.time()
#print("The time when code has ended: ", end_time_code)
print("total time: " ,(end_time_code - start_time_code), "seconds")

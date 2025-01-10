import time     

def decorator(input_num):

    global start_time_code
    start_time_code = time.time()
    print("The time when code is started : ", start_time_code)
    
    while True:
        print("\n To calculate :\n")
        print(" 1. ADD\n 2. SUBTRACT\n 3. MULTIPLY\n 4. DIVIDE \n 0. EXIT")
        
        choice = int(input("Enter the operation choice you want to perform: "))
        print("The choice is : ", choice)
        if choice == 1:
            num1 = input_num()
            num2 = input_num()
            print("The addition is: ", f"{num1} + {num2} = {num1 + num2}")
        elif choice == 2:
            num1 = input_num()
            num2 = input_num()
            print("The subtraction is: ", f"{num1} - {num2} = {num1 - num2}")
        elif choice == 3:
            num1 = input_num()
            num2 = input_num()
            print("The multiply is: ", f"{num1} * {num2} = {num1 * num2}")
        elif choice == 4:
            num1 = input_num()
            while True:
                num2 = input_num()
                if y == 0:
                    raise ZeroDivisionError("Invalid Input")
                else:
                    break
            print("The division is: ", f"{num1} / {num2} = {num1 / num2}")
        elif choice == 0:
            break
        elif choice > 4:
            print("Please Enter the choice between 1 to 4")
        else:
            raise TypeError("Only integers are allowed")
        
@decorator	   
def input_num():
    num1 = float(input("Enter the number: "))
    return num1

global end_time_code
end_time_code = time.time()
print("The time when code has ended: ", end_time_code)

total_time = start_time_code - end_time_code
print("Total time taken by the code to run: ", abs(total_time))

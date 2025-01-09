def fact(n):
    if n == 0:
        return 1
    if n > 1:
        return fact(n) * fact(n - 1)

def main():
    num = int(input("Enter the number"))
    return fact(num)
    
main()
    
# This code will throw the error when it reches to fact(n - 1) as discussed in the session


#Correct way to solve the factorial by recursion
'''
def factorial(num):
    if num < 0:
        raise TypeError("Invalid Input")
    if num == 0 or num == 1:
        return 1
    if num > 1:
        return num * factorial(num-1)
        
def main():
    num = int(input("Enter the number: "))
    print("the factorial of", num , "is: ", factorial(num))

main()

'''



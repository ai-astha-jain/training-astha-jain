def armstrong(num):
    number = str(num)
    num = len(number)
    output = 0
    for i in number:
        output = output + int(i) ** num
        
    if output == int(number):
        return True
    else:
        return False

num = int(input("Enter the number: "))        
print(armstrong(num))

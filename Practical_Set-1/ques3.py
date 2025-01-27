a = 10
b = 20
print(a and b)  # 20  why? = and operator returns second operand if first is truthy, if first operand is none, 0, false  then it returns first operand 
print(a or b)   # 10  why? = vice versa of "and"

if False:
    print("It is False")
else:
    print("It is True")
# Output =  It is True


if [ ]:
    print("It is Blank")
else:
    print("It is Something else")
#Output =  It is Something else


if [ [ ] ]:
    print("It is Blank")
else:
    print("It is Something else")
#Output =  It is Blank

if [ False ]:
    print("It is Blank")
else:
    print("It is Something else")
#Output =  It is Blank



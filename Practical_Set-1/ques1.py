print([]*3)     # []

print((2)**2)    # 4


#print({3:1} * 2)
''' print({3:1} * 2)
TypeError: unsupported operand type(s) for *: 'dict' and 'int'
'''


#print(['a', 'b', 'c'] + ‘rf’)

'''
File "/home/odoo/Downloads/Practical_Set-1/ques1.py", line 7
    print(['a', 'b', 'c'] + ‘rf’)
                            ^
SyntaxError: invalid character '‘' (U+2018)
'''


Z = ['P', 'L', ']' ] 
Z += 'SE'
print(Z)

# ['P', 'L', ']', 'S', 'E']


print(('a', 'b', 'c') * 2)
# ('a', 'b', 'c', 'a', 'b', 'c')

print([{}] * 2)
# [{}, {}]


#print(‘123’ + 2)
'''
File "/home/odoo/Downloads/Practical_Set-1/ques1.py", line 34
    print(‘123’ + 2)
          ^
SyntaxError: invalid character '‘' (U+2018)
'''

#print((2, 4) ** 2)
'''
File "/home/odoo/Downloads/Practical_Set-1/ques1.py", line 37, in <module>
    print((2, 4) ** 2)
TypeError: unsupported operand type(s) for ** or pow(): 'tuple' and 'int'
'''


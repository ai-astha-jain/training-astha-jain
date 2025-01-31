string1 = input("Enter the string: ")
print("\n The string is: ", string1)
string1 = string1.lower()
words = string1.split(" ")
#print("\nThe list of string is: ",words)    

repeated_words = []

print("\nThe repeated words are: ", )
    
for i in range(0, len(words)):
    count = 1
    for j in range(i+1, len(words)):
        if(words[i] == words[j]):
            count = count + 1
            words[j] = '0'
    if count>1 and words[i] != '0':
        repeated_words.append(words[i])
        
        
print(repeated_words)        

result = "#".join(repeated_words)
print("\nThe desired output is:", result) 
    

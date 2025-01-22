noun_list = []
article_list = ["a", "an"]

noun_range = int(input("Enter the number of noun: "))
for i in range(noun_range):
    noun_name = str(input("Enter the noun name: "))
    noun_list.append(noun_name)
    i += 1
    
print("The nouns are: ", noun_list)
print("The articles are: ", article_list)

index_list = int(input("Enter the index of list to retrieve value: "))


def valid_string(noun_list):
    global article_a
    global article_an
    global word_and
    if not noun_list[index_list][0] in 'aeiou':
         article_a = "a"
         return article
    if noun_list[index_list][0] in 'aeiou'
         article_an = "an"
        return article 
    if noun_list[-2]:
        word_and = "and"
        noun_list[-2].format(word_and)
    
    return valid_string      
      
desired_string = "{}"

print(noun_list[0][0])
print(noun_list[1][0])
print(noun_list[2][0])

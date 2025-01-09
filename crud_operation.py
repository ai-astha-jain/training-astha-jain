country = []

c = int(input("Enter the range:"))

i = 0

for i in range(c):
    country_name = input("Enter the country name :")
    country.append(country_name)
    i += 1
    
print("Country :", country)

state = []

s = int(input("Enter the range:"))

j = 0

for j in range(s):
    state_name = input("Enter the state name :")
    state.append(state_name)
    j += 1
    
print("State :", state)
    
city = []

x = int(input("Enter the range:"))

k = 0

for k in range(x):
    city_name = input("Enter the city name :")
    city.append(city_name)
    k += 1
    
print("City :", city)

def add_country():
    print("\nAdding the country to the list")
    ques = int(input("\nDo you want to add country 0/1 :"))
    print(ques)
    if ques == 1 :
        country_name = input("Enter the country name : ")
        country.append(country_name)  
    elif ques == 0:
        add()
    else:
        raise NameError("Only integers are allowed")
    
    print("Country: ", country)
        
def add_state():
    print("\nAdding the state to the list")
    ques = int(input("\nDo you want to add state 0/1 :"))
    print(ques)
    if ques == 1 :
        state_name = input("Enter the state name : ")
        state.append(state_name)    
    elif ques == 0:
        add()
    else:
        raise NameError("Only integers are allowed")
    
    print("State: ", state)
        
def add_city():
    print("\nAdding the city to the list")
    ques = int(input("\nDo you want to add city 0/1 :"))
    print(ques)
    if ques == 1 :
        city_name = input("Enter the city name : ")
        city.append(city_name)    
    elif ques == 0:
        add()
    else:
        raise NameError("Only integers are allowed")
    
    print("City: ", city)
    
def delete_country():
    ques = int(input("Do you want to delete a country? 0/1: "))
    if ques == 1 :
        country_removal = input("Write the country name you want to remove: ")
        print(country_removal)
        country.remove(country_removal)
    elif ques == 0:
        delete()
    else:
    	raise NameError("Only integers are allowed")
    print("Country: ", country)
    
def delete_state():
    ques = int(input("Do you want to delete a state? 0/1: "))
    if ques == 1 :
        state_removal = input("Write the state name you want to remove: ")
        print(state_removal)
        state.remove(state_removal)
    elif ques == 0:
        delete()
    else:
    	raise NameError("Only integers are allowed")
    print("State: ", state)
    
def delete_city():
    ques = int(input("Do you want to delete a city? 0/1: "))
    if ques == 1 :
        city_removal = input("Write the city name you want to remove: ")
        print(city_removal)
        city.remove(city_removal)
    elif ques == 0:
        delete()
    else:
    	raise NameError("Only integers are allowed")
    print("City: ", city)
    
def update_country():
    ques = int(input("do you want to update the country: "))
    if ques == 1:
        old_country = input("Which country do you want to replace: ")
        new_country = input("Enter the country name you want to replace with: ")
        updated_country_list = list(map(lambda upt: new_country if upt == old_country else upt, country))
    elif ques == 0:
        update()
    else:
        raise NameError("Only integers are allowed")
    print("Updated Country: ", updated_country_list)

def update_state():
    ques = int(input("do you want to update the state: "))
    if ques == 1:
        old_state = input("Which state do you want to replace: ")
        new_state = input("Enter the state name you want to replace with: ")
        updated_state_list = list(map(lambda upt: new_state if upt == old_state else upt, state))
    elif ques == 0:
        state()
    else:
        raise NameError("Only integers are allowed")
    print("Updated State: ", updated_state_list)

def update_city():
    ques = int(input("do you want to update the city: "))
    if ques == 1:
        old_city = input("Which city do you want to replace: ")
        new_city = input("Enter the city name you want to replace with: ")
        updated_city_list = list(map(lambda upt: new_city if upt == old_city else upt, city))
    elif ques == 0:
        update()
    else:
        raise NameError("Only integers are allowed")
    print("Updated City: ", updated_city_list)

def add():
    print("\nTo add :")
    print("\t1. Country \n")
    print("\t2. State \n")
    print("\t3. City \n")
    print("\t4. Exit\n")
    
    id_input = int(input("Enter the id you want to add in :"))
    print(id_input)
    if id_input == 1:
        add_country()
    elif id_input == 2:
        add_state()
    elif id_input == 3:
        add_city()
    elif id_input == 4:
        menu()
    else:
        raise NameError("Only integers are allowed")


        
def delete():
    print("\n To delete: ")
    print("\t1. Country \n")
    print("\t2. State \n")
    print("\t3. City \n")
    print("\t4. Exit\n")
    
    id_input = int(input("Enter the id you wanna delete in: "))
    print(id_input)
    if id_input == 1:
        delete_country()
    elif id_input == 2:
        delete_state()
    elif id_input == 3:
        delete_city()
    elif id_input == 4:
        menu()
    else:
        raise NameError("Only integers are allowed")
        
def update():
    print("\n To update: ")
    print("\t1. Country \n")
    print("\t2. State \n")
    print("\t3. City \n")
    print("\t4. Exit\n")
    
    id_input = int(input("Enter the id you want to update in: "))
    print(id_input)
    if id_input == 1:
        update_country()
    elif id_input == 2:
        update_state()
    elif id_input == 3:
        update_city()
    elif id_input == 4:
        menu()
    else:
        raise NameError("Only integers are allowed")
        
    
def menu():
    print("\nTo make changes in the program: ")
    print("\t1. ADD\n")
    print("\t2. DELETE\n")
    print("\t3. UPDATE\n")
    
    id_input = int(input("Enter the id you want to change in: "))
    print(id_input)
    if id_input == 1:
        add()
    elif id_input == 2:
    	delete()
    elif id_input == 3:
    	update()
    else:
        raise NameError("Only integers inputs are allowed")
                     
menu()                                                                                             

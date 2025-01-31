# Initialize the nested dictionary
locations = {}

# Add country, state, and city functions
def add_country():
    country_name = input("Enter the country name: ")
    if country_name not in locations:
        locations[country_name] = {}
    else:
        print(f"Country '{country_name}' already exists.")
    print("Countries:", list(locations.keys()))

def add_state():
    country_name = input("Enter the country name to add state to: ")
    if country_name in locations:
        state_name = input("Enter the state name: ")
        if state_name not in locations[country_name]:
            locations[country_name][state_name] = []
        else:
            print(f"State '{state_name}' already exists in country '{country_name}'.")
        print(f"States in {country_name}:", list(locations[country_name].keys()))    
    else:
        print(f"Country '{country_name}' does not exist. Add the country first.")

def add_city():
    country_name = input("Enter the country name: ")
    if country_name in locations:
        state_name = input("Enter the state name: ")
        if state_name in locations[country_name]:
            city_name = input("Enter the city name: ")
            if city_name not in locations[country_name][state_name]:
                locations[country_name][state_name].append(city_name)
            else:
                print(f"City '{city_name}' already exists in state '{state_name}'.")
            print(f"Cities in {state_name}, {country_name}: {locations[country_name][state_name]}")    
        else:
            print(f"State '{state_name}' does not exist. Add the state first.")
    else:
        print(f"Country '{country_name}' does not exist. Add the country first.")
    
# Delete functions
def delete_country():
    country_name = input("Enter the country name to delete: ")
    if country_name in locations:
        del locations[country_name]
        print(f"Deleted country '{country_name}'.")
        
    else:
        print(f"Country '{country_name}' not found.")

def delete_state():
    country_name = input("Enter the country name: ")
    if country_name in locations:
        state_name = input("Enter the state name to delete: ")
        if state_name in locations[country_name]:
            del locations[country_name][state_name]
            print(f"Deleted state '{state_name}' from country '{country_name}'.")
        else:
            print(f"State '{state_name}' not found in country '{country_name}'.")
    else:
        print(f"Country '{country_name}' not found.")

def delete_city():
    country_name = input("Enter the country name: ")
    if country_name in locations:
        state_name = input("Enter the state name: ")
        if state_name in locations[country_name]:
            city_name = input("Enter the city name to delete: ")
            if city_name in locations[country_name][state_name]:
                locations[country_name][state_name].remove(city_name)
                print(f"Deleted city '{city_name}' from state '{state_name}' in country '{country_name}'.")
            else:
                print(f"City '{city_name}' not found in state '{state_name}'.")
        else:
            print(f"State '{state_name}' not found.")
    else:
        print(f"Country '{country_name}' not found.")

# Update functions
def update_country():
    old_country = input("Enter the old country name: ")
    if old_country in locations:
        new_country = input("Enter the new country name: ")
        locations[new_country] = locations.pop(old_country)
        print(f"Updated country '{old_country}' to '{new_country}'.")
    else:
        print(f"Country '{old_country}' not found.")

def update_state():
    country_name = input("Enter the country name: ")
    if country_name in locations:
        old_state = input("Enter the old state name: ")
        if old_state in locations[country_name]:
            new_state = input("Enter the new state name: ")
            locations[country_name][new_state] = locations[country_name].pop(old_state)
            print(f"Updated state '{old_state}' to '{new_state}' in country '{country_name}'.")
        else:
            print(f"State '{old_state}' not found in country '{country_name}'.")
    else:
        print(f"Country '{country_name}' not found.")

def update_city():
    country_name = input("Enter the country name: ")
    if country_name in locations:
        state_name = input("Enter the state name: ")
        if state_name in locations[country_name]:
            old_city = input("Enter the old city name: ")
            if old_city in locations[country_name][state_name]:
                new_city = input("Enter the new city name: ")
                cities = locations[country_name][state_name]
                cities[cities.index(old_city)] = new_city
                print(f"Updated city '{old_city}' to '{new_city}' in state '{state_name}', country '{country_name}'.")
            else:
                print(f"City '{old_city}' not found in state '{state_name}'.")
        else:
            print(f"State '{state_name}' not found in country '{country_name}'.")
    else:
        print(f"Country '{country_name}' not found.")

# Print function to display the nested dictionary
def print_locations():
    if locations:
        print("\n--- Locations ---")
        for country, states in locations.items():
            print(f"Country: {country}")
            for state, cities in states.items():
                print(f"  State: {state}")
                print(f"    Cities: {', '.join(cities)}")
    else:
        print("No locations available.")

# Menu to navigate
def menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Add")
        print("2. Delete")
        print("3. Update")
        print("4. Print Locations")
        print("5. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter the integers only.")
            continue
        if choice == 1:
            add_menu()
        elif choice == 2:
            delete_menu()
        elif choice == 3:
            update_menu()
        elif choice == 4:
            print_locations()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

# Sub-menu for adding
def add_menu():
    while True:
        print("\n--- Add Menu ---")
        print("1. Add Country")
        print("2. Add State")
        print("3. Add City")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter the integers only.")
            continue
    
        if choice == 1:
            add_country()
        elif choice == 2:
            add_state()
        elif choice == 3:
            add_city()
        elif choice == 4:
            break
        else:
            print("Invalid choice, try again.")

# Sub-menu for deleting
def delete_menu():
    while True:
        print("\n--- Delete Menu ---")
        print("1. Delete Country")
        print("2. Delete State")
        print("3. Delete City")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter the integers only.")
            continue
        if choice == 1:
            print_locations()
            delete_country()
        elif choice == 2:
            print_locations()
            delete_state()
        elif choice == 3:
            print_locations()
            delete_city()
        elif choice == 4:
            break
        else:
            print("Invalid choice, try again.")

# Sub-menu for updating
def update_menu():
    while True:
        print("\n--- Update Menu ---")
        print("1. Update Country")
        print("2. Update State")
        print("3. Update City")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter the integers only.")
            continue
        if choice == 1:
            print_locations()
            update_country()
        elif choice == 2:
            print_locations()
            update_state()
        elif choice == 3:
            print_locations()
            update_city()
        elif choice == 4:
            break
        else:
            print("Invalid choice, try again.")

# Run the menu
menu()

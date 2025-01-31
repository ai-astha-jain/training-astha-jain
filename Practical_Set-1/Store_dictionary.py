class Store:
    def __init__(self):
        self.store_dictionary = {}
        
    def add_store_data(self):
        while True:
            # Enter the number of shelves you want in store in integer
            try:
                num_shelves = int(input("Enter the number of shelves: "))
            except ValueError:
                print("Please enter the valid integer")
                return True         
            # loop to enter shelf name and store data into dictionary
            for i in range(num_shelves):
                shelf_name = input("Enter the shelf name: ")
                if not shelf_name.isdigit():
                    self.store_dictionary[shelf_name] = {}
                else:
                    print("Please enter the valid input")
                    return True            
                # Enter the number of products in the specific shelf
                try:
                    num_products = int(input(f"Enter the number of products you want in {shelf_name}: "))
                except ValueError:
                    print("Please enter the valid integer")
                    return True
                #Number of products in the choosen shelf
                for i in range(num_products):
                    product_name = input(f"Enter the product name in {shelf_name}: ")
                    if not product_name.isdigit():
                        self.store_dictionary[shelf_name][product_name] = {}
                    else:
                        print("Enter the valid product name.")
                        return True      
                
                    # months for which data is available
                    try:
                        months = list(map(str,input(f"Enter the months for {product_name} in {shelf_name} (comma separated): ").split(',')))
                    except ValueError:
                        print("Please enter the months separated by comma.")
                        return True
                        
                    for month in months:
                        month = month.strip()
                        try:
                            costs = list(map(int, input(f"Enter the cost price for {product_name} in {month} (space separated): ").split()))
                        except ValueError:
                            print("Please enter the cost price with the space and enter a valid integer.")
                            return True
                            
                        try:
                            sale_percentage = int(input(f"Enter the sale percentage for {product_name} in {month}: "))
                        except ValueError:
                            print("Please enter the sale percentage in integer.")
                            return True
                            
                        self.store_dictionary[shelf_name][product_name][month] ={
                            "cost_price": costs,
                            "sale_price": [cp + (cp*sale_percentage/100) for cp in costs]
                        }
            break          
                               
    # method to show data in dictionary                    
    def view_store_data(self):
        """ Displays the stored data """
        print("\n--- Store Data ---")
        for shelf, products in self.store_dictionary.items():
            print(f"\nShelf: {shelf}")
            for product, months in products.items():
                print(f"  Product: {product}")
                if 'category' in months:
                    print(f"    Category: {months['category']}")
                for month, data in months.items():
                    if isinstance(data, dict):  # To avoid printing the 'category' as a month
                        print(f"    {month}:")
                        print(f"      Cost Prices: {data['cost_price']}")
                        print(f"      Sale Prices: {data['sale_price']}")

     # method to update sale price for all the products               
    def update_product_sale_price_for_all(self, new_sale_percentage):
        for shelf, product, in self.store_dictionary.items():
            for product,months in product.items():
                for month, data in months.items():
                    data['sale_price'] = [cp + (cp*new_sale_percentage/100) for cp in data["cost_price"]]
    
    # method to update sale price for all the products with a given specific shelf                
    def update_sale_price_for_shelf(self, shelf_name, new_sale_percentage_shelf):
        if shelf_name in self.store_dictionary:
            for product, months in self.store_dictionary[shelf_name].items():
                for month, data in months.items():
                    data['sale_price'] = [cp + (cp*new_sale_percentage_shelf/100) for cp in data["cost_price"]]
    
    #method to add a category to the specific product                
    def set_category_product(self, shelf_name, product_name):
        if shelf_name in self.store_dictionary:
            if product_name in self.store_dictionary[shelf_name]:
                category = input(f"Enter the category for {product_name} in shelf {shelf_name}: ")
                
                self.store_dictionary[shelf_name][product_name]["category"] = category
                
                print(f"Category '{category}' has been set for product '{product_name}' in shelf '{shelf_name}'.")
            else:
                print(f"Product {product_name} not found in shelf {shelf_name}. ")
        else:
            print(f"Shelf {shelf_name} not found.")
    
    #method to create a new shelf        
    def create_new_shelf(self):
        shelf_name = input("Enter the shelf name:")
        if not shelf_name.isdigit():
            self.store_dictionary[shelf_name] = {}
        else:
            print("Please enter the valid input")
            return True  
        if shelf_name not in self.store_dictionary:
            print(f"Shelf {shelf_name} not found. Create new shelf.")
            self.store_dictionary[shelf_name] = {}
            
            # Enter the number of products in the specific shelf
            try:
                num_products = int(input(f"Enter the number of products you want in {shelf_name}: "))
            except ValueError:
                print("Please enter the valid integer")
                return True
            
            #Number of products in the choosen shelf
            for i in range(num_products):
                product_name = input(f"Enter the product name in {shelf_name}: ")
                if not product_name.isdigit():
                    self.store_dictionary[shelf_name][product_name] = {}
                else:
                    print("Enter the valid product name.")
                    return True 
                
                # months for which data is available
                months = input(f"Enter the months for {product_name} in {shelf_name} (comma separated): ").split(',')
                    
                for month in months:
                    month = month.strip()
                    costs = list(map(int, input(f"Enter the cost price for {product_name} in {month} (space separated): ").split()))
                    try:
                        sale_percentage = int(input(f"Enter the sale percentage for {product_name} in {month}: "))
                    except ValueError:
                        print("Please enter the sale percentage in integer.")
                        return True    
                    self.store_dictionary[shelf_name][product_name][month] ={
                        "cost_price": costs,
                        "sale_price": [cp + (cp*sale_percentage/100) for cp in costs]
                    }
        else:
            print(f"Shelf {shelf_name} exists. ")
    
    # method to reset the cost price of all the products in all the shelf to zero        
    def reset_cost_price(self):
        for shelf, products, in self.store_dictionary.items():
            for product, months in products.items():
                for month, data in months.items():
                    data['cost_price'] = [0*cp for cp in data["cost_price"]]
                    data['sale_price'] = [0*cp for cp in data["cost_price"]]
    
    # method to find max and min cost price of the product                
    def max_min_price(self, shelf_name, product_name):
        if shelf_name in self.store_dictionary:
            if product_name in self.store_dictionary[shelf_name]:
                max_price = None
                min_price = None
                for month,data in self.store_dictionary[shelf_name][product_name].items():
                    if isinstance(data, dict):
                        if "cost_price" in data:
                            max_month = max(data["cost_price"])
                            min_month =min(data["cost_price"])
                    
                            if max_price is None or max_month > max_price:
                                max_price = max_month    
                            if min_price is None or min_month < min_price:
                                min_price = min_month    
                print(f"The maximum price for {shelf_name} for {product_name} is {max_price}.") 
                print(f"The minimum price for {shelf_name} for {product_name} is {min_price}.") 
    
    # method to create average cost and average profit of product in a given month            
    def average_cost_profit(self,shelf_name, product_name, month_name):
        if shelf_name in self.store_dictionary:
            if product_name in self.store_dictionary[shelf_name]:
                if month_name in self.store_dictionary[shelf_name][product_name]:
                    data = self.store_dictionary[shelf_name][product_name][month_name]
                    
                    cost_price = data["cost_price"]
                    sale_price = data["sale_price"]
                    
                    if cost_price and sale_price:
                        total_cost = sum(cost_price)
                        total_sale = sum(sale_price)
                        
                        total_profit = total_sale - total_cost
                        
                        average_cost = total_cost/len(cost_price)
                        average_profit = total_profit/len(cost_price)
                        
                        print(f"Average cost for {product_name} in shelf {shelf_name} for month {month_name}: {average_cost: .2f}")    
                        print(f"Average sales profit for {product_name} in shelf {shelf_name} for month {month_name}: {average_profit: .2f}")    
                    else:
                        print("\nNo valid cost price and sale price")
                else:
                    print(f"No month {month_name} is found.")
                    
            else:
                print(f"No product {product_name} found.")
        else:
            print(f"No shelf {shelf_name} found")

    #method to show the menu to select any method to use.
    def menu(self):
        while True:
            print('''\n
                1. Add data to the dictionary
                2. View data in the dictionary
                3. Update the sale price with given percentage.
                4. Update the sale price for a given shelf with a given percentage.
                5. Set a category for a given product.
                6. Create a shelf.
                7. Reset the cost price to 0 for a given shelf, product, month.
                8. Update maximum and minmum price with the shelf name and product name
                
                9. Average cost and sales profit based on specific product for specific month.
                0. Exit 
                ''')
            
            choice = input("Enter the choice(0-9): ")
            if choice.isdigit():
                choice = int(choice)
            else:
                print("Invalid choice. Please enter the valid choice")
                continue
            
            if choice == 1:
                self.add_store_data()
                self.view_store_data()
            elif choice == 2:
                self.view_store_data()
            elif choice == 3:
                new_sale_percentage = float(input("Enter the new sale percentage to update for all products: "))
                self.update_product_sale_price_for_all(new_sale_percentage)
                self.view_store_data()
            elif choice == 4:
            	shelf_name = input("Enter the shelf name: ")
            	product_name = input("Enter the product name: ")
            	new_sale_percentage_shelf = float(input("Enter the new sale percentage to update for all products: "))
            	self.update_product_sale_price_for_all(new_sale_percentage_shelf)
            	self.view_store_data()
            elif choice == 5:
                shelf_name = input("Enter the shelf name: ")
                product_name = input("Enter the product name: ")
                self.set_category_product(shelf_name, product_name)
                self.view_store_data()
            elif choice == 6:
                self.create_new_shelf()
                self.view_store_data()
            elif choice == 7:
                self.reset_cost_price()
                self.view_store_data()
            elif choice == 8:
                shelf_name = input("Enter the shelf name: ")
                product_name = input("Enter the product name: ")
                self.max_min_price(shelf_name,product_name)
                self.view_store_data()
            elif choice == 9:
                shelf_name = input("Enter the shelf name: ")
                product_name = input("Enter the product name: ")
                month_name = input("Enter the month name: ")
                self.average_cost_profit(shelf_name, product_name, month_name)
                self.view_store_data()
            elif choice == 0:
                break
            else:
                print("PLease enter the valid integer.")
                continue
            '''elif choice == 4:    
            elif choice == 5:
            elif choice == 6:
            elif choice == 7:
            elif choice == 8:
            elif choice == 9:'''
             
                    
store = Store()
store.menu()



                                                               
            

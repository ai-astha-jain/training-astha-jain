class input_sales():
    def __init__(self, product_id, product_name, sale_amount, sale_date):
        self.product_id = product_id
        self.product_name = product_name
        self.sale_amount = sale_amount
        self.sale_date = sale_date
        
        
        
        
class show_sales(input_sales):
    def __init__(self,  product_id, product_name, sale_amount, sale_date, total_sale, average_sale, highest_sell_product):
        super().__init__(product_id, product_name, sale_amount, sale_date)
        self.total_sale = total_sale
        self.average_sale = average_sale
        self.highest_sell_product = highest_sell_product
           
    def totalSale(self, sale_amount):
        return sum(self.sale_amount)
    def avgSale(self, sale_amount):
        return (sum(self.sale_amount))/count(sale_amount) 
    def highSellProduct(self,product_id):
        return count(self.product_id)
                 
      
info_dictionary = {}
info_sale_dictionary = {}
      
  

def input_sale(product_id):
        product_name = input("Enter the product name: ")
        sale_amount = int(input("Enter the sale amount: "))
        sale_date = input("Enter the sale date(yy-mm-dd): ")       
        inputSales = input_sales(product_id, product_name, sale_amount, sale_date)
        
        
  
while True:
    print('''
        1. Add to dictionary
        2. View Dictionary
        3. View sales dictionary
    ''')
    choice = int(input("Enter the choice: "))
    if choice == 1:
        product_id = int(input("Enter the product_id: "))
    elif choice == 2:
        for key,values in info_dictionary.items():
            print(f"{key}:{values}")   
    elif choice == 3:
        for key,values in info_sale_dictionary.items():
            print(f"{key}:{values}")
    else:
        raise TypeError("Enter the correct choice")  
    
    input_sale(product_id)    
 
inputSales = input_sales(product_id, product_name, sale_amount, sale_date)
showSales = show_sales(total_sale, average_sale, highest_sell_product) 
                
info_dictionary[product_id] = {
    "product_name": product_name,
    "sale_amount": sale_amount,
    "sale-date": sale_date
    }
      
info_sale_dictionary = {
    "total_sale": showSales.totalSale(),
    "average_sale": showSales.avgSale(),
    "highest_sell_product": showSales.highSellProduct()
} 



 
 


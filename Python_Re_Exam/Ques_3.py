# calculate the total sale of the day
def total(sales_data):
    pass
          
      
      
#function to find the date where sale_amount is maximum
def highest(sales_data):
    amount_list = []
    for data in sales_data:
        amount_list.append(data['sale_amount'])
    for i in amount_list:
        max_amount = 0
        if i > max_amount:
            max_amount = i
    return sales_data[amount_list.index(max_amount)]     


# input dictionary
sales_data = [
    {"product_id": 101, "product_name": "Smartphone", "sale_amount": 500, "sale_date":"2025-01-01"},
    {"product_id": 102, "product_name": "Laptop", "sale_amount": 300, "sale_date":"2025-01-01"},
    {"product_id": 101, "product_name": "Smartphone", "sale_amount": 400, "sale_date":"2025-01-02"},
    {"product_id": 103, "product_name": "Smartwatch", "sale_amount": 700, "sale_date":"2025-01-02"},
]


output = {}

# drivers code
total_sale_per_day = total(sales_data)
HighestSellingDay = highest(sales_data)
output = {
    #"Total Sales Per Day": {'sale_date': total_sale_per_day["sale_date"], 'total_sale_amount' :total_sale_per_day("product_id")},
    "Highest Selling Day": HighestSellingDay["sale_date"]
}

print(output)

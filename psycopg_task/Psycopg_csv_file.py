import psycopg2

conn = psycopg2.connect(
	database = "product_orders",
	user = "odoo",
	host = "127.0.0.1",
	password = "odoo",
	port = 5432
)

cur = conn.cursor()




cur.execute('''
	create table customers(
		customer_id serial primary key,
		customer_name varchar(100),
		customer_email varchar(100)
	);
''')

cur.execute("insert into customers(customer_name, customer_email) values('Alice', 'alice@email.com'),('Bob' , 'bob@email.com'),('Charlie','charlie@email.com');")


cur.execute('''
	create table products(
		product_id serial primary key,
		product_name varchar(100),
		product_price int
	);
''')



cur.execute(" insert into products(product_name, product_price) values('Mobile', 30),('Laptop', 70),('TV', 90);
 ")


cur.execute('''
	create table orders(
		id serial primary key,
		customer_id serial,
		constraint customer_id foreign key (customer_id)
    		references customers(customer_id),
    		product_id serial,
    		constraint product_id foreign key (product_id)
    		references products(product_id),
		quantity int,
		order_date date
	);
''')

cur.execute("insert into orders(id, customer_id, product_id, quantity, order_date) values(1, 1, 2, 1, '2025-01-01'),(2, 2, 1, 3, '2025-01-02'); ")

#Query 1

cur.execute(" select c.customer_id, c.customer_name, p.product_id, p.product_name, p.product_price, COALESCE(o.quantity, 0) as quantity, o.order_date from customers c left join products p on p.product_id = c.customer_id left join orders o on o.id = c.customer_id; ")


#Query 2

cur.execute(" select p.product_id, p.product_name from orders o right join products p on  p.product_id = o.product_id where p.product_id NOT IN (select product_id from orders);
 ")


#Query 3

cur.execute(" select c.customer_id, c.customer_name, p.product_id, p.product_name, p.product_price*COALESCE(o.quantity, 1) as total_value, o.order_date from customers c left join products p on p.product_id = c.customer_id left join orders o on o.id = c.customer_id where p.product_price > 50;  ")

cur.execute("select * from customers;")
cur.execute("select * from products;")
cur.execute("select * from orders;")


conn.commit()

cur.close()
conn.close()

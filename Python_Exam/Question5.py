# taking input of number of list can be seated in a row
row = []
 
no_of_seats = int(input("Enter the number of seat user want: "))
 
# if the seat is empty then it is 0 
global empty_seat 
global occupied_seat 

empty_seat = 0
occupied_seat = 1

def row_list(row): 
    for i in range(no_of_seats):
        global seats
        seats = int(input("Enter the seats(0,1): "))        
        if seats != 0 or seats != 1:
            row.append(seats)
            i = i+1              
        else:
            print("Only mentioned input is allowed")
        
    print("The row is: ",row)   
    
def count_max_person(row, occupied_seat):
    max_occupied_seat = row.count(occupied_seat)
    print("The number of occupied seats are: ",max_occupied_seat)

row_list(row)

count_max_person(row, occupied_seat)
 
 
 

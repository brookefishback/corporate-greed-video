#I want a point of sale solution for Family Video’s rivals
#At very minimum it needs to have a stock of 5 rentable titles
#Employee should be able to register new users, rent titles to users, and check titles back in
#Any other functionality is secondary but welcome.
#I don’t care how you implement checking in/out, but no shortcuts/fakery
#Don’t have to have it done by next week, but iterate so that you can at least demo features as they are completed

from datetime import date

#CREATE CLASSES - CUSTOMERS, TRANSACTIONS + MOVIES
class Customer:
    def __init__(self, name, number):
        self.name = name
        self.number = number

class Transaction:
    def __init__(self, transaction, time, total):
        self.transaction = transaction
        self.time = time
        self.total = total

class Movie:
    def __init__(self, title, price):
        self.title = title
        self.price = price

#CREATE MASTER TITLE LIST
title_list = [
    "Gone With the Wind", 
    "Shawshank Redemption", 
    "Pulp Fiction", 
    "Cruel Intentions," 
    "The Godfather", 
    "Casablanca"]

#MASTER CLIENT LIST - ADD ALL NEW CLIENTS TO THIS LIST
client_list = []

#MENU ITEM 1 - REGISTER NEW CLIENT
def new_client():
    input_new_client_name = input("Input the new client's name: ")
    input_new_client_number = input("Phone number: ")
    new_client_to_list = Order(input_new_client_name,input_new_client_number)
    client_list.append(new_client_to_list)
    for list_number, clients in enumerate(client_list,1):
        print(str(list_number), ".", clients.name),
        print("    Phone number: ", clients.number),
        print()

#MENU ITEM 2 - CHECK OUT FUNCTION
## NEED TO MAKE THIS INTO SEPERATE FUNCTIONS
## NOT SURE WHAT TO DO WITH TRANSACTION
def check_out(client_list):
    print("Please select the client that wants to rent a movie. ")
    for list_number, clients in enumerate(client_list,1):
        print(str(list_number), ".", clients.name),
        print("    Phone number: ", clients.number),
        print()

    select_from_client_list = input("")
    select_from_client_list = int(select_from_client_list) - 1
    print("You have selected "+client_list[select_from_client_list].name), 
    print()
    for list_number, movies in enumerate(title_list,1):
        print(str(list_number), ".", movies)

    select_from_movie_list = input("Please select the movie rented: ")
    select_from_movie_list = int(select_from_movie_list) - 1
    print("You have selected "+title_list[select_from_movie_list])
    title_rental = input("Would you like to rent this movie? Y or N: ")
    if title_rental == "Y":
        Order.title = title_list[select_from_movie_list]
        client_list[select_from_client_list].title = Order.title
        print(client_list[select_from_client_list].name + " has rented " + client_list[select_from_client_list].title)
        Order.time = time_and_date_stamp()
        client_list[select_from_client_list].time = Order.time
# NEED TO CONVERT TO 3 or 5 DAYS?        
        print(client_list[select_from_client_list].time)
        Order.title = ''
        Order.time = ''
#   elif title_rental == "N":





#MENU ITEM 3 - CHECK IN TITLE FUNCTION
#def check_in():

#MENU ITEM 4 - VIEW ORDER FUCNTION - PRINTS ORDER LIST FOR SALESMAN
#def view_orders():

#CREATE MAIN MENU FUNTION
def main():
    menu = {}
    menu['1']="Register New Client" 
    menu['2']="Title - Check Out"
    menu['3']="Title - Check In"
    menu['4']="View Orders"
    menu['5']="Exit/Quit"

#CREATE TIME STAMP
def time_and_date_stamp():
    today_date = date.today()
    return today_date

#CREATE ORDER NUMBER
def transaction_number():
    transaction_order = len(active_titles) + 1
    return transaction_order

#WHILE AND IF STATEMENTS TO HANDLE SALESMEN'S MENU CHOICES
user=True
while user:
    print ("""
    1. Register New Client
    2. Check Out
    3. Check In
    4. View Orders
    5. Exit/Quit
    """)
    answer=input("What would you like to do? ") 
    if answer=="1": 
        new_client()
    elif answer=="2":
        check_out(client_list)
    elif answer=="3":
        check_in()
    elif answer=="4":
        view_orders()
    elif answer=="5":
        print("\n Goodbye")
        break
    elif answer !="":
        print("\n Invaild Entry")

if __name__ == "__main__":
    main()
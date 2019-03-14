## NEED TO MAKE A PRICE FOR MOVIES IN CLASS 
## NEED TO MAKE A TOTAL AMOUNT FOR TRANSACTION IN CHECKOUT
## NEED TO MAKE A TIMEDELTA IN ORDER TO DETERMINE WHEN MOVIE IS DUE
## TRYING TO FIGURE OUT THE PROCESS OF CLIENT CHECK-IN SHOULD BE
## VIEW ORDER NEEDS TO EXTRA TLC

from datetime import datetime

class Customer:
    def __init__(self, name, number):
        self.name = name
        self.number = number

class Transaction:
    def __init__(self, name, number, movie, time):
        self.name = name
        self.number = number
        self.movie = movie
        self.time = time

class Movie:
    def __init__(self, title):
        self.title = title
#        self.price = price

title_list = [
    "Gone With the Wind", 
    "Shawshank Redemption", 
    "Pulp Fiction", 
    "Cruel Intentions", 
    "The Godfather", 
    "Casablanca"]

def inventory_creation():
    movie_inventory = []
    for titles in title_list:
            movie_inventory.append(Movie(titles))
    return movie_inventory

available_titles = inventory_creation()

client_list = []
transaction_list = []
time_of_rental = datetime.now()

def list_of_available_clients():
    for list_number, clients in enumerate(client_list,1):
        print(str(list_number), ".", clients.name),
        print("    Phone number: ", clients.number),

def list_of_available_movies():
    for list_number, movies in enumerate(available_titles,1):
        print(str(list_number), ".", movies.title)

def display_transaction_list():
    for list_number, finalization in enumerate(transaction_list,1):
        print(str(list_number), ".", 
        "Client Name: " + finalization.name + '\n'
        "Client Phone Number: " + finalization.number + '\n'
        "Movie Rented: " + finalization.movie + '\n'
        "Date Rented: " + finalization.time)  

def new_client():
    input_new_client_name = input("Input the new client's name: ")
    input_new_client_number = input("Phone number: ")
    new_client_to_list = Customer(input_new_client_name,input_new_client_number)
    client_list.append(new_client_to_list)
    print()

def check_out(client_list):
    print("Please select the client that wants to rent a movie. ")
    list_of_available_clients()
    print()

    select_from_client_list = input("")
    select_from_client_list = int(select_from_client_list) - 1
    print("You have selected " + client_list[select_from_client_list].name), 
    print()

    list_of_available_movies()

    select_from_movie_list = input("Please select the movie you'd like rented: ")
    select_from_movie_list = int(select_from_movie_list) - 1
    print("You have selected " + available_titles[select_from_movie_list].title)
    title_rental = input("Would you like to rent this movie? Y or N: ")

    selected_client_name = client_list[select_from_client_list].name
    selected_client_number = client_list[select_from_client_list].number
    selected_movie = available_titles[select_from_movie_list].title
 
    if title_rental == "Y":
        transaction_list.append(Transaction(selected_client_name, selected_client_number, selected_movie, time_of_rental.strftime("%m/%d/%Y")))
        print(selected_client_name + " has rented " + selected_movie + ".")

    elif title_rental == "N":
        return

#MENU ITEM 3 - CHECK IN TITLE FUNCTION
#def check_in():


#MENU ITEM 4 - VIEW ORDER FUCNTION - PRINTS ORDER LIST FOR SALESMAN
def view_orders(transaction_list):
    client_check = []
    print("Please type S to search for a client.")
    print("Type ALL if you'd like to see the whole list.")
    view_order_type = input("")
    if view_order_type == "S":
        client_phone_number = input("Please input the client's number. ")
        for check in range(len(transaction_list)):
            if len(transaction_list) > 0:
                client_check.append(transaction_list.pop(0))
                matching_client = [c for c in client_check if c.number == client_phone_number]
                if matching_client:
                    print("Client Name: " + matching_client[0].name + '\n'
                    "Movie Rented: " + matching_client[0].movie + '\n'
                    "Date Rented: " + matching_client[0].time)
                    print()
                    transaction_list.append(client_check.pop(0))

                else:
                    transaction_list.append(client_check.pop(0))
        
            elif len(transaction_list) < 1:
                print ("There are currently no Clients.")
                return

    elif view_order_type == "ALL":
        display_transaction_list()

    else:
        return


#CREATE MAIN MENU FUNTION
def main():
    menu = {}
    menu['1']="Register New Client" 
    menu['2']="Title - Check Out"
    menu['3']="Title - Check In"
    menu['4']="View Orders"
    menu['5']="Exit/Quit"


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
        view_orders(transaction_list)
    elif answer=="5":
        print("\n Goodbye")
        break
    elif answer !="":
        print("\n Invaild Entry")

if __name__ == "__main__":
    main()
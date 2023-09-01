# Railway Management System in Python with Text File Handling

# Function to display the main menu
def display_menu():
    print("Welcome to the Railway Management System!")
    print("1. Login")
    print("2. View Trains")
    print("3. Add Train")
    print("4. Edit Train")
    print("5. Delete Train")
    print("6. Book Ticket")
    print("7. Cancel Ticket")
    print("8. Exit")
    
users = {'rishi': '2610', 'ayush': '2727', 'meet': '9999'}

#Function to login in your system
def login():
    username = input('Enter username: ')
    password = input('Enter password: ')
    if username in users and users[username] == password:
        print('Login successful!')
        print("Hello"+" "+username)
        print("Welcome")
    else:
        print("Invalid username and password")

# Function to display all trains
def view_trains():
    with open("trains.txt", "r") as file:
        data = file.readlines()
        if not data:
            print("No trains found!")
        else:
            for i, train in enumerate(data):
                print(f"{i + 1}. {train}")

# Function to add a new train
def add_train():
    train_name = input("Enter train name: ")
    train_number = input("Enter train number: ")
    train_route = input("Enter train route: ")
    with open("trains.txt", "a") as file:
        file.write(f"{train_name}, {train_number}, {train_route}\n")
        print("Train added successfully!")

# Function to edit an existing train
def edit_train():
    train_number = input("Enter train number to edit: ")
    with open("trains.txt", "r") as file:
        data = file.readlines()
    with open("trains.txt", "w") as file:
        for train in data:
            if train_number in train:
                train_name = input("Enter new train name: ")
                train_route = input("Enter new train route: ")
                file.write(f"{train_name}, {train_number}, {train_route}\n")
                print("Train updated successfully!")
            else:
                file.write(train)

# Function to delete a train
def delete_train():
    train_number = input("Enter train number to delete: ")
    with open("trains.txt", "r") as file:
        data = file.readlines()
    with open("trains.txt", "w") as file:
        for train in data:
            if train_number not in train:
                file.write(train)
        print("Train deleted successfully!")

# Function to book a ticket
def book_ticket():
    train_number = input("Enter train number: ")
    with open("trains.txt", "r") as file:
        data = file.readlines()
    for train in data:
        if train_number in train:
            ticket_name = input("Enter passenger name: ")
            ticket_age = input("Enter passenger age: ")
            ticket_gender = input("Enter passenger gender: ")
            pass_number=int(input("Enter passenger mobile number: "))
            with open(f"{train_number}.txt", "a") as file:
                file.write(f"{ticket_name}, {ticket_age}, {ticket_gender}, {pass_number}\n")
                print("Ticket booked successfully!")
            break
    else:
        print("Train not found!")

# Function to cancel a ticket
def cancel_ticket():
    train_number = input("Enter train number: ")
    with open("trains.txt", "r") as file:
        data = file.readlines()
    for train in data:
        if train_number in train:
            ticket_name = input("Enter passenger name: ")
            with open(f"{train_number}.txt", "r") as file:
                tickets = file.readlines()
            with open(f"{train_number}.txt", "w") as file:
                for ticket in tickets:
                    if ticket_name not in ticket:
                        file.write(ticket)
                print("Ticket cancelled successfully!")
            break
    else:
        print("Train not found!")

def main():
    while True:
        print("\t\t\t\t\t WELCOME TO RAILWAY MANAGEMENT SYSTEM \t\t\t\t\t\n\n")
        display_menu()
        choice = int(input("Enter your choice:"))
        if choice==1:
            login()
        elif choice == 2:
            view_trains()
        elif choice == 3:
            add_train()
        elif choice == 4:
            edit_train()
        elif choice == 5:
            delete_train()
        elif choice == 6:
            book_ticket()
        elif choice == 7:
            cancel_ticket()
        elif choice == 8:
            print("Thank you for using the Railway Management System!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()
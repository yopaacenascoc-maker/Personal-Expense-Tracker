repeat = True
registered = False
username = ""
password = ""
expenses = []

while repeat:
    print("\n--- Expense System ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        registered = True
        print("Registered successfully!")

    elif choice == "2":
        user = input("Username: ")
        pw = input("Password: ")

        if user == username and pw == password:
            print("Login successful!")
            logged_in = True

            while logged_in:
                print("\n1. Add Expense")
                print("2. View Expenses")
                print("3. Logout")
                pick = input("Enter choice: ")

                if pick == "1":
                    item = input("Expense name: ")
                    amount = input("Amount: ")
                    expenses.append(item + " - " + amount)
                    print("Expense added!")

                elif pick == "2":
                    print("\n--- Expense List ---")
                    if len(expenses) == 0:
                        print("No expenses yet.")
                    else:
                        for i in range(len(expenses)):
                            print(f"{i+1}. {expenses[i]}")

                elif pick == "3":
                    print("Logged out.")
                    logged_in = False

                else:
                    print("Invalid choice.")
        else:
            print("Invalid login!")

    elif choice == "3":
        print("Goodbye!")
        repeat = False

    else:
        print("Invalid input.")

from operations import *

while True:
    print("\n1. Add User")
    print("2. Add Expense")
    print("3. View Expenses")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        add_user(name)

    elif choice == 2:
        user_id = int(input("User ID: "))
        amount = float(input("Amount: "))
        category = input("Category: ")
        desc = input("Description: ")
        date = input("Date (YYYY-MM-DD): ")

        add_expense(user_id, amount, category, desc, date)

    elif choice == 3:
        user_id = int(input("User ID: "))
        expenses = view_expenses(user_id)

        print("Total:", total_expense(expenses))
        print("Category:", category_spending(expenses))
        print("Highest:", highest_expense(expenses))
        print("Monthly:", monthly_report(expenses))
        print("Insight:", smart_insight(expenses))

    elif choice == 4:
        break
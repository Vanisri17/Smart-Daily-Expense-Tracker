import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"
BUDGET = 3000


# Create CSV file
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                ["Date", "Category", "Description", "Amount"]
            )


# Add a new expense
def add_expense():
    category = input("Enter category: ")
    description = input("Enter description: ")

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than zero!")
            return

    except ValueError:
        print("Please enter a valid amount!")
        return

    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print("Expense added successfully!")


# View all expenses
def view_expenses():
    print("\n----- All Expenses -----")

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader, None)

        found = False

        for row in reader:
            if row:
                print("Date:", row[0])
                print("Category:", row[1])
                print("Description:", row[2])
                print("Amount: Rs.", row[3])
                print("----------------------")
                found = True

        if not found:
            print("No expenses found!")


# Show expense summary
def show_summary():
    total = 0

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                total += float(row["Amount"])
            except (ValueError, TypeError):
                continue

    print("\n----- Expense Summary -----")
    print("Total Expense: Rs.", round(total, 2))
    print("Monthly Budget: Rs.", BUDGET)
    print("Remaining Budget: Rs.", round(BUDGET - total, 2))

    if total > BUDGET:
        print("Warning! Budget exceeded!")
    else:
        print("You are within your budget!")


# Main menu
if __name__ == "__main__":
    create_file()

    while True:
        print("\n===== Smart Daily Expense Tracker =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expense Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            show_summary()

        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice! Try again.")

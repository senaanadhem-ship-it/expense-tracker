import csv
import os
from datetime import date

FILE = "expenses.csv"


def add_expense():
    item = input("Enter expense name: ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))

    file_exists = os.path.exists(FILE)

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["Date", "Item", "Category", "Amount"])

        writer.writerow([date.today(), item, category, amount])

    print("Expense saved successfully!")


def view_expenses():
    if not os.path.exists(FILE):
        print("No expenses found.")
        return

    total = 0

    with open(FILE, "r", newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            print(
                row["Date"], "|",
                row["Item"], "|",
                row["Category"], "| ₹",
                row["Amount"]
            )
            total += float(row["Amount"])

    print("Total expenses: ₹", round(total, 2))


while True:
    print("\n--- EXPENSE TRACKER ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        try:
            add_expense()
        except ValueError:
            print("Please enter a valid amount.")
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.")

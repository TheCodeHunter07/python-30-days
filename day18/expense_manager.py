import datetime
import csv
import json
import os



# JSON FILE CONFIGURATION

FILE_NAME = "expenses.json"



# LOAD EXPENSES FROM JSON

def load_expenses():

    if os.path.exists(FILE_NAME):

        with open(FILE_NAME, "r") as file:
            return json.load(file)

    return []



# SAVE EXPENSES TO JSON

def save_expenses():

    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

# EXPENSE STORAGE


expenses = load_expenses()

next_id = max(
    (expense["id"] for expense in expenses),
    default=0
) + 1



# 1. ADD EXPENS

def add_expense():

    global next_id

    print("\n========== ADD EXPENSE ==========")

    # Validate amount
    while True:

        try:
            amount = int(input("Enter the Amount: "))

            if amount <= 0:
                print("Amount must be greater than zero!")
                continue

            break

        except ValueError:
            print("Enter a valid integer amount!")

    # Get category and description
    category = input("Enter the Category: ").strip()
    description = input("Enter the Description: ").strip()

    # Validate date
    while True:

        try:
            date = input("Enter the Date (YYYY-MM-DD): ")

            datetime.datetime.strptime(date, "%Y-%m-%d")

            break

        except ValueError:
            print("Enter a valid date in YYYY-MM-DD format!")

    # Create expense dictionary
    expense = {
        "id": next_id,
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }

    # Add expense to list
    expenses.append(expense)

    # Save expenses to JSON
    save_expenses()

    next_id += 1

    print("\nExpense added successfully!")


# 2. VIEW ALL EXPENSES


def view_expenses():

    print("\n========== ALL EXPENSES ==========")

    if not expenses:
        print("No expenses found!")
        return

    print("\n" + "=" * 85)

    print(
        f"{'ID':<5} "
        f"{'Amount':<12} "
        f"{'Category':<15} "
        f"{'Description':<25} "
        f"{'Date':<15}"
    )

    print("=" * 85)

    total_amount = 0

    for expense in expenses:

        print(
            f"{expense['id']:<5} "
            f"{expense['amount']:<12} "
            f"{expense['category']:<15} "
            f"{expense['description']:<25} "
            f"{expense['date']:<15}"
        )

        total_amount += expense["amount"]

    print("=" * 85)

    print(f"Total Expenses: ₹{total_amount}")


# ==========================================
# 3. CATEGORY-WISE EXPENSES
# ==========================================

def category_wise():

    print("\n========== CATEGORY-WISE EXPENSES ==========")

    if not expenses:
        print("No expenses found!")
        return

    category_totals = {}

    for expense in expenses:

        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:

            category_totals[category] += amount

        else:

            category_totals[category] = amount

    for category, total in category_totals.items():

        print(f"{category:<15} ₹{total}")

    print("----------------------------------")


# 4. FILTER EXPENSES BY MONTH


def filter_by_month():

    print("\n========== FILTER BY MONTH ==========")

    while True:

        try:
            month = input("Enter the Month (YYYY-MM): ")

            datetime.datetime.strptime(month, "%Y-%m")

            break

        except ValueError:
            print("Enter the Month in format YYYY-MM!")

    filtered_expenses = []

    for expense in expenses:

        if expense["date"].startswith(month):

            filtered_expenses.append(expense)

    if not filtered_expenses:
        print("No expenses found for this month!")
        return

    total = 0

    print("\n" + "=" * 85)

    print(
        f"{'ID':<5} "
        f"{'Amount':<12} "
        f"{'Category':<15} "
        f"{'Description':<25} "
        f"{'Date':<15}"
    )

    print("=" * 85)

    for expense in filtered_expenses:

        print(
            f"{expense['id']:<5} "
            f"{expense['amount']:<12} "
            f"{expense['category']:<15} "
            f"{expense['description']:<25} "
            f"{expense['date']:<15}"
        )

        total += expense["amount"]

    print("=" * 85)

    print(f"Total Expenses: ₹{total}")


# ==========================================
# 5. DELETE EXPENSE
# ==========================================

def delete_expense():

    print("\n========== DELETE EXPENSE ==========")

    if not expenses:
        print("No expenses found!")
        return

    while True:

        try:
            expense_id = int(input("Enter the Expense ID: "))

            if expense_id <= 0:
                print("Enter a valid positive ID!")
                continue

            break

        except ValueError:
            print("Enter the Expense ID in integers!")

    selected_expense = None

    for expense in expenses:

        if expense["id"] == expense_id:

            selected_expense = expense
            break

    if selected_expense is None:

        print("This expense does not exist!")
        return

    print("\nExpense Details:")

    print("ID:", selected_expense["id"])
    print("Amount:", selected_expense["amount"])
    print("Category:", selected_expense["category"])
    print("Description:", selected_expense["description"])
    print("Date:", selected_expense["date"])

    confirmation = input(
        "\nAre you sure you want to delete? (yes/no): "
    )

    if confirmation.lower() == "yes":

        expenses.remove(selected_expense)

        # Update JSON file
        save_expenses()

        print("Expense deleted successfully!")

    else:

        print("Deletion cancelled!")



# 6. EXPORT EXPENSES TO CSV


def export_csv():

    print("\n========== EXPORT EXPENSES ==========")

    if not expenses:
        print("No expenses found!")
        return

    with open("expenses.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "ID",
            "Amount",
            "Category",
            "Description",
            "Date"
        ])

        for expense in expenses:

            writer.writerow([
                expense["id"],
                expense["amount"],
                expense["category"],
                expense["description"],
                expense["date"]
            ])

    print("Expenses exported successfully to expenses.csv!")
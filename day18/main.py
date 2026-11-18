from expense_manager import (
    add_expense,
    view_expenses,
    category_wise,
    filter_by_month,
    delete_expense,
    export_csv
)


# ==========================================
# MAIN APPLICATION
# ==========================================

def main():

    while True:

        print("\n========== PERSONAL EXPENSE TRACKER ==========")

        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Category-wise Expenses")
        print("4. Filter Expenses by Month")
        print("5. Delete Expense")
        print("6. Export Expenses to CSV")
        print("7. Exit")

        print("==============================================")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":

            add_expense()

        elif choice == "2":

            view_expenses()

        elif choice == "3":

            category_wise()

        elif choice == "4":

            filter_by_month()

        elif choice == "5":

            delete_expense()

        elif choice == "6":

            export_csv()

        elif choice == "7":

            print("\nThank you for using Personal Expense Tracker!")
            break

        else:

            print("Invalid choice! Please select between 1 and 7.")


# ==========================================
# PROGRAM EXECUTION
# ==========================================

if __name__ == "__main__":

    main()
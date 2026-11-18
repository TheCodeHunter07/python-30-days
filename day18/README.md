# 💰 Personal Expense Tracker

A command-line based Personal Expense Tracker built using Python. This application allows users to manage their daily expenses, categorize spending, filter expenses by month, and export expense reports to CSV.

The application uses JSON for persistent data storage, so expenses remain saved even after closing the program.

## 🚀 Features

- **Add Expense:** Add expenses with amount, category, description, and date.
- **View Expenses:** Display all expenses in a formatted table.
- **Category-wise Summary:** Calculate total expenses for each category.
- **Monthly Filtering:** Filter expenses based on a specific month.
- **Delete Expense:** Delete an expense using its unique ID.
- **CSV Export:** Export expense records into a CSV file.
- **JSON Storage:** Automatically load and save expenses between program runs.
- **Input Validation:** Handle invalid amounts and dates without crashing.

## 🛠️ Technologies Used

- Python 3
- JSON
- CSV
- datetime module
- os module

## 📁 Project Structure

```text
stage3-expense-tracker/
│
├── main.py
├── expense_manager.py
├── expenses.json
├── expenses.csv
└── README.md
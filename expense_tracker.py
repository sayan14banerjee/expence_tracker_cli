import argparse
import json
import os
from datetime import datetime
import csv

DATA_FILE = "expenses.json"

# storage helper
def load_expenses():
    if not os.path.exists(DATA_FILE):
        return {"expenses": [], "budgets": {}}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)
    
def save_expenses(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# main features
def add_expense(description, amount, category=None):
    data = load_expenses()
    today = datetime.now().date()
    new_id = len(data["expenses"]) + 1
    expense = {
        "id": new_id,
        "description": description,
        "amount": amount,
        "category": category,
        "date": today.isoformat()
    }
    data["expenses"].append(expense)
    save_expenses(data)
    print(f"Expense added successfully (ID: {new_id})")

def update_expense(expense_id, description=None, amount=None, category=None):
    data = load_expenses()
    for expense in data["expenses"]:
        if expense["id"] == expense_id:
            if description:
                expense["description"] = description
            if amount:
                expense["amount"] = amount
            if category:
                expense["category"] = category
            save_expenses(data)
            print(f"Expense ID {expense_id} updated successfully")
            return
    print(f"Expense ID {expense_id} not found")
def delete_expense(expense_id):
    data = load_expenses()
    for i, expense in enumerate(data["expenses"]):
        if expense["id"] == expense_id:
            del data["expenses"][i]
            save_expenses(data)
            print(f"Expense ID {expense_id} deleted successfully")
            return
    print(f"Expense ID {expense_id} not found")
def list_expenses():
    data = load_expenses()
    if not data["expenses"]:
        print("No expenses recorded.")
        return
    for expense in data["expenses"]:
        print(f"ID: {expense['id']}, Description: {expense['description']}, Amount: {expense['amount']}, Category: {expense.get('category', 'N/A')}, Date: {expense['date']}")
def summary(month=None):
    data = load_expenses()
    total = 0
    for expense in data["expenses"]:
        expense_date = datetime.fromisoformat(expense["date"])
        if month is None or expense_date.month == month:
            total += expense["amount"]
    print(f"Total expenses{' for month ' + str(month) if month else ''}: {total}")
def set_budget(month, amount):
    data = load_expenses()
    data["budgets"][str(month)] = amount
    save_expenses(data)
    print(f"Budget for month {month} set to {amount}")

def check_budget(month):
    data = load_expenses()
    budget = data["budgets"].get(str(month))
    if budget is None:
        print(f"No budget set for month {month}")
        return
    total = 0
    for expense in data["expenses"]:
        expense_date = datetime.fromisoformat(expense["date"])
        if expense_date.month == month:
            total += expense["amount"]
    print(f"Budget for month {month}: {budget}, Total expenses: {total}, Remaining: {budget - total}")
def export_expenses(file_path="expenses_export.csv"):
    data = load_expenses()
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['id', 'description', 'amount', 'category', 'date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for expense in data["expenses"]:
            writer.writerow(expense)
    print(f"Expenses exported to {file_path}")

# command-line interface

parser = argparse.ArgumentParser(prog="expense-tracker", description="CLI Expense Tracker App")
sub = parser.add_subparsers(dest="command")

# ADD
add_cmd = sub.add_parser("add")
add_cmd.add_argument("--description", required=True)
add_cmd.add_argument("--amount", required=True, type=float)
add_cmd.add_argument("--category", required=False)

# UPDATE
update_cmd = sub.add_parser("update")
update_cmd.add_argument("--id", required=True, type=int)
update_cmd.add_argument("--description", required=False)
update_cmd.add_argument("--amount", required=False, type=float)
update_cmd.add_argument("--category", required=False)

# DELETE
delete_cmd = sub.add_parser("delete")
delete_cmd.add_argument("--id", required=True, type=int)

# LIST
list_cmd = sub.add_parser("list")

# SUMMARY
summary_cmd = sub.add_parser("summary")
summary_cmd.add_argument("--month", required=False, type=int)

# SET BUDGET
set_budget_cmd = sub.add_parser("set-budget")
set_budget_cmd.add_argument("--month", required=True, type=int)
set_budget_cmd.add_argument("--amount", required=True, type=float)

# CHECK BUDGET
check_budget_cmd = sub.add_parser("check-budget")
check_budget_cmd.add_argument("--month", required=True, type=int)

# EXPORT
export_cmd = sub.add_parser("export")
export_cmd.add_argument("--file", required=False, default="expenses_export.csv")

args = parser.parse_args()

if args.command == "add":
    add_expense(args.description, args.amount, args.category)
elif args.command == "update":
    update_expense(args.id, args.description, args.amount, args.category)
elif args.command == "delete":
    delete_expense(args.id)
elif args.command == "list":
    list_expenses()
elif args.command == "summary":
    summary(args.month)
elif args.command == "set-budget":
    set_budget(args.month, args.amount)
elif args.command == "check-budget":
    check_budget(args.month)
elif args.command == "export":
    export_expenses(args.file)
else:
    parser.print_help()
    
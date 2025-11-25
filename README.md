# 💸 Expense Tracker CLI

A simple and powerful [**Command-Line Expense Tracker**](https://github.com/sayan14banerjee/expence_tracker_cli) application built using Python.  
It allows users to add, update, delete, view, and summarize expenses — all from the terminal.

---

## 🚀 Features

- Add new expenses with description and amount  
- Update or delete existing expenses  
- View all expenses in a table format  
- View total summary of all expenses  
- View summary for a specific month  
- Categorize expenses (e.g., Food, Travel, Shopping)  
- Set monthly budgets and get warnings when exceeded  
- Export all expenses to a CSV file  
- Stores all data in a simple JSON file (`expenses.json`)

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/expense-tracker-cli.git
cd expense-tracker-cli
```

## 🛠 Commands & Usage
### ➕ Add Expense
```bash
python expense_tracker.py add --description "Lunch" --amount 20
```

### ✏ Update Expense
```bash
python expense_tracker.py update --id 1 --amount 50
```

### ❌ Delete Expense
```bash
python expense_tracker.py delete --id 2
```

### 📋 List All Expenses
```bash
python expense_tracker.py list
```

### 📂 List by Category
```bash
python expense_tracker.py list --category Food
```

### 📊 Summary of All Expenses
```bash
python expense_tracker.py summary
```

### 📅 Summary for Specific Month
```bash
python expense_tracker.py summary --month 8
```

### 🎯 Set Monthly Budget
```bash
python expense_tracker.py budget --month 8 --amount 5000
```

### 📤 Export to CSV
```bash
python expense_tracker.py export --filename expenses.csv
```

### 📁 Data Storage

#### All data is stored in:
```bash 
expenses.json
```

#### Format includes:

- ID

- Date

- Description

- Amount

- Category

## 🤝 Contributing

Feel free to open issues or submit pull requests.
Suggestions and improvements are always welcome!

## 📜 License

This project is open-source and available under the MIT License.

## ⭐ Acknowledgements

Built as a practice project to improve:

- CLI development

- File handling

- Data management

- Python application structure

## Happy Tracking! 💰

If you want a **longer, more detailed README**, or want to include **screenshots, badges, or examples**

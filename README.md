# Personal Expense Tracker (Python + Pandas)

A simple command-line based Personal Expense Tracker built using **Python** and **Pandas**.
This project allows users to record, view, delete, and analyze their expenses efficiently.

---

##  Features

*  Add new transactions
*  View all transactions
*  Delete transactions using ID
*  Generate monthly expense reports
*  Category-wise spending analysis
*  Persistent storage using CSV file

---

##  Technologies Used

* Python
* Pandas
* OS Module (for file handling)

---

##  Project Structure

```
├── main.py                # Main Python script
├── Transaction.csv       # Stores all transactions (auto-created)
└── README.md             # Project documentation
```

---

## ⚙️ How It Works

### 1. Data Storage

* All transactions are stored in a CSV file (`Transaction.csv`)
* If the file does not exist, it is automatically created

---

### 2. Available Operations

When you run the program, you get the following options:

```
Enter 0 to View Transaction  
Enter 1 to Add Transactions  
Enter 2 to Delete Transaction  
Enter 3 to Generate Monthly Report  
```

---

### 3. Functionalities

####  Add Transaction

* Automatically assigns a unique ID
* Takes input:

  * Date (DD/MM/YY)
  * Amount
  * Category
  * Description (optional)

---

####  View Transactions

* Displays all stored transactions in tabular format

---

####  Delete Transaction

* Deletes transaction using **ID**
* Updates CSV file after deletion

---

####  Monthly Report

* Generates report for a specific month
* Shows:

  * Total spending
  * Category-wise spending
  * Highest spending category
  * Highest expense amount

---

##  Example Output

```
Report For Month : 3
Total Spending : 5000
Total Spending Category Wise :
   Category  Amount
0  Food      2000
1  Travel    3000

Highest Spending Category : Travel
Highest Amount : 3000
```

---

##  Key Concepts Used

* Pandas DataFrame operations
* File handling with CSV
* Data filtering and grouping
* Exception handling
* Modular programming using functions


##  Author

**Govind Sharma**
B.Tech (AI & Data Science)

---

##  Acknowledgment

This project is built as part of learning **Python and Data Analysis fundamentals**.

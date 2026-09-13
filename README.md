# BLAST! EXPENSE TRACKER
#### Video Demo:  <URL HERE>
## Description
Blast! Expense Tracker is my CS50 Python project. It's an expense tracker app that uses "Custom TKinter" for the interface. The application uses two primary files, "etracker.py" and "expenseDB.py" to implement 3 classes, "ExpenseTracker", "TransForm" and "Expenses" to build its functionalities. 

The expense tracker helps a user add any expense or income from any date and by default shows a summary of the month. It shows the list of transactions and gives the ability to filter transactions by start and end dates. It also has "Edit" and "Delete" functions for each transaction. Users can add new transactions and edit existing ones from the transaction form. The tracker also gives the ability to change the  currency symbol (no currency conversion).

By default it shows current month's transactions in the transaction list, but users can change dates to see oa larger list.
# Architecture

he expense tracker uses 3 classes:
- ExpenseTracker: This class is the primary application that creates the expense tracker, along with the database functions.
-Expenses: This class auto-creates the SQLite3 database required.
-TransForm:   
Trans_Form: This class creates a transaction form with fields such as date, type, amount, category, and description and allows users to add transactions to the database.
### Functions
There are many functions that were implemented as part of the tracker. Some of the important ones are listed below.
#### ExpenseTracker class:
-	Build_ui(): This function helps build the user interface of the tracker, it uses “Custom TKinter” which is Python’s GUI building library to build multiple frames to display list of expenses, the transaction form, sidebar, topbar with logo, etc. Build_sidebar(), build_summary(), etc., are called from within here to display those items.
-	Build_summary(): This functions builds a monthly summary of expenses/income and shows the balance. It has green/red background based on whether the balance is positive or negative for the month.
-	Build_expense_table(): This function generates an expense table with data it gets from the database. By default it shows the details of the current month’s transactions. But users are given date pickers to select a wider range of dates.
-	Change_currency(): This function allows users to set a different currency symbol. It doesn’t have conversion options, only symbol change. Currency conversion is not a feature of the app.
#### Trans_Form class
-	Build_form_ui(): This function builds the UI of the form. The Trans_Form class is a subclass of CTkFrame, so it can be displayed on any GUI element. The form UI has fields for date, type, category, amount, and description. It also has two buttons to save or cancel the transaction.
-	Validate_form(): This function validates all the data the user puts in the fields. If any data is missing or incorrect, it alerts users using an alert box, implemented using CTkMessagebox class.
-	Save_trans(): This function calls the database’s function to add a validated transaction to the database.
-	Cancel_trans(): The function resets the transaction box and cancels the transaction.
-	Reset_form(): Removes all data from the form fields and resets it back to default setting. Called by default after a transaction is saved or cancelled.
-	Edit_trans(): The function is called when “Edit” button on transaction table is clicked. It populates all the details of the transaction in the same form, and allows users to make edits. 

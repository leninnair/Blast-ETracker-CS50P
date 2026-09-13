from etracker import ExpenseTracker
from expenseDB import Expenses
import sqlite3


#-----------------------------------IMPORTANT-----------------------------------------------------#
#   This file has been created as a requirement by CS50 for the project submission.               #
#   The actual functionality of the application is implemented in etracker.py, expenseDB.py.      #
#   This file has main and 3 other functions, which have minimal functionality along with tests.  #
#-------------------------------------------------------------------------------------------------#

etracker = ExpenseTracker()  # Creates the expense tracker as a global var, so all functions can access it.
expenses = Expenses()

def main():
    etracker.mainloop() # Runs the expense tracker.

def add_dummy_transaction(transaction: tuple):
    # transaction tuple contains dummy values of date, type, category, amount, description.
    if len(transaction) != 5:
        raise IndexError("transaction length wrong.")
    if not all(transaction[:4]):
        raise ValueError("Invalid date, type, category, or amount")
    try:
        amount = float(transaction[3])
    except ValueError:
        raise ValueError("error in amount")
    if transaction[1] not in ("Income", "Expense"):
        raise ValueError("Invalid type")
        
    try:
        expenses.save_transaction(transaction) # Saves the transaction in the database.

    except Exception:
        expenses.db.rollback()
        return
    expenses.db.commit()

def fetch_trans():
    transactions = expenses.data_generator() # Calls the function to generate data (yield)
    return transactions

def delete_trans(amt): # Deletes all transactions of a particular value.
    try:
        expenses.cursor.execute("DELETE FROM transactions WHERE amount = ?", (amt,))
    except sqlite3.DatabaseError:
        expenses.db.rollback()
        return
    expenses.db.commit()


if __name__ == "__main__":
    main()

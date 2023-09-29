#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk
from tkinter import messagebox

class BudgetTracker:
    def __init__(self, master):
        self.master = master
        self.master.title("Personal Budget Tracker")
        self.master.geometry("1000x600")
        self.master.configure(bg="white")  

        self.expenses_frame = tk.Frame(master, bg="white")
        self.expenses_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.expenses_label = tk.Label(self.expenses_frame, text="Expenses", font=('arial', 15, 'bold'), bg="white", fg="black")
        self.expenses_label.pack(pady=(20, 0))

        self.expenses_listbox = tk.Listbox(self.expenses_frame, font=('Arial', 15), width=30, height=15, bg="#FFFFFF", fg="#000000", selectbackground="#CD853F", selectforeground="#FFFFFF")
        self.expenses_listbox.pack()

        self.budget_label = tk.Label(master, text="Enter Budget:", font=('arial',15,'bold'),bg="white", fg="black")  
        self.budget_label.pack(pady=(20,0))

        self.budget_entry = tk.Entry(master)
        self.budget_entry.pack(pady=(0,20))

        self.add_expense_button = tk.Button(master, text="➕ Add Expense", font=('arial',15,'bold'), command=self.add_expense, bg="black", fg="white")  
        self.add_expense_button.pack()

        self.view_expense_button = tk.Button(master, text="👁 View Expenses", font=('arial',15,'bold'), command=self.view_expenses, bg="black", fg="white")  
        self.view_expense_button.pack()

        self.calculate_button = tk.Button(master, text="🧮 Calculate Remaining Budget", font=('arial',15,'bold'), command=self.calculate_remaining_budget, bg="black", fg="white")  
        self.calculate_button.pack()

        self.analysis_button = tk.Button(master, text="📊 Expense Analysis", font=('arial',15,'bold'), command=self.expense_analysis, bg="black", fg="white")  
        self.analysis_button.pack()

        self.quit_button = tk.Button(master, text="Quit", font=('arial',15,'bold'), command=master.quit, bg="black", fg="white")  
        self.quit_button.pack()

        self.expenses = []
        self.budget = 0

    def add_expense(self):
        try:
            expense = float(self.budget_entry.get())
            self.expenses.append(expense)
            self.expenses_listbox.insert(tk.END, f"${expense:.2f}")
            messagebox.showinfo("Success", "Expense added successfully!")
            self.budget_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def view_expenses(self):
        if self.expenses:
            expenses_text = "\n".join([f"${expense:.2f}" for expense in self.expenses])
            messagebox.showinfo("Expenses", f"Your expenses:\n{expenses_text}")
        else:
            messagebox.showinfo("Expenses", "No expenses recorded yet.")

    def calculate_remaining_budget(self):
        total_expenses = sum(self.expenses)
        remaining_budget = self.budget - total_expenses
        messagebox.showinfo("Budget Calculation", f"Total Expenses: ${total_expenses:.2f}\nRemaining Budget: ${remaining_budget:.2f}")

    def expense_analysis(self):
        if self.expenses:
            average_expense = sum(self.expenses) / len(self.expenses)
            max_expense = max(self.expenses)
            min_expense = min(self.expenses)
            messagebox.showinfo("Expense Analysis", f"Average Expense: ${average_expense:.2f}\nMax Expense: ${max_expense:.2f}\nMin Expense: ${min_expense:.2f}")
        else:
            messagebox.showinfo("Expense Analysis", "No expenses recorded yet.")

if __name__ == "__main__":
    root = tk.Tk()
    budget_tracker = BudgetTracker(root)
    root.mainloop()



# In[ ]:





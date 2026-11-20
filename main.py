#  "Expense Tracker Project"

expensesList = [] #list of expenses in form of dictionary
print("Welcome to Expense Traker :")

while True:
    print("=====MENU======")
    print("1. Add Expenses")
    print("2, View All Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice = int(input("Enter Your Choice: "))
 
 # 1. ADD EXPENSES
    if(choice == 1):
        date=input("Date of expense")
        category = input("Type of expense")
        description = input("Expense details")
        amount = float(input("Enter amount"))

        expense = {
            "date" : date,
            "category" : category,
            "description" : description, 
            "amount" : amount,

        }

        expensesList.append(expense)
        print("\n Done bro. Expense is added succesfully")
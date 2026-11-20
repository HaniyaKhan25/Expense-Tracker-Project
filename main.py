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

#    2. VIEW ALL EXPENSES
    elif(choice == 2):
        if(len(expensesList) == 0):
            print("No expenses added")
        else:
            print("======= Here are all your expenses =========")
            count  = 1
            for eachExpense in expensesList:
                print(f"Expense numbe r {count} -> {eachExpense["date"]}, {eachExpense["category"]}, {eachExpense["description"]}, {eachExpense["amount"]} " )
                count = count + 1
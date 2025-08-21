#steps plan:
    #ask the user for total monthly income
    #income has to be >0 if 0 or not a number re-ask for income
    #list for expenses
    #loop: ask about expenses and add to list of expenses
    #expense has to be >=0 and a number if not re-ask for it
    #add q to quit from the loop
    #calculate the total of expenses and make it in variable
    #calculate the difference between income and expenses
    #the difference is saving(variable) for the month
    #calculate the rate of saving and expenses ==> rates = value * 100 / income
    #print the result income saving and expenses and rates of each format : 2 dicimals
    #If savings rate ≥ 20% → print “Good job!”, else → print “Try to save more.”

#Implementation

while True:
    try:
        income = float(input("What's your monthly income?: "))
        if income > 0:
            break
        print("Income must be greater than 0.")
    except ValueError:
        print("Please enter a number (e.g., 7500).")

expenses = []

while True:
    raw = input('Enter an expense amount (or "q" to finish): ').strip()
    if raw.lower() == "q":
        break
    try:
        amount = float(raw)
        if amount < 0:
            print("Expense must be ≥ 0. Try again.")
            continue
        expenses.append(amount)
    except ValueError:
        print('Please enter a number (e.g., 1200) or "q".')

total_expenses = sum(expenses)
savings = income - total_expenses

expenses_rate = (total_expenses * 100) / income
savings_rate = (savings * 100) / income

print("----- SUMMARY -----")
print(f"Income:          {income:10.2f}")
print(f"Expenses:        {total_expenses:10.2f}  ({len(expenses)} items)")
print(f"Savings:         {savings:10.2f}")
print(f"Expense rate:    {expenses_rate:10.2f}%")
print(f"Savings rate:    {savings_rate:10.2f}%")

if total_expenses > income:
    print("Warning! You spent more than you earned.")

print("Good job!" if savings_rate >= 20 else "Try to save more.")
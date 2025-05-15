transactions = []
balance = 0.0
total_income = 0.0
total_expense = 0.0

def get_transaction():
    amount = float(input("Enter the amount"))
    type_input = input("Is it income or expense")
    return{"type": type_input, "amount": amount}

def calculate_totals(transactions):
    balance = 0.0
    total_income = 0.0
    total_expense = 0.0 
    for t in transactions:
      if t["type"] == "income":
        balance += t["amount"]
        total_income += t["amount"]
      elif t["type"] == "expense": 
        balance -= t["amount"]
        total_expense += t["amount"]
    return balance, total_expense, total_income

def show_summary(balance, total_expense, total_income):
    print(f"Your current balance is {balance}. Your expenses are {total_expense} and your income is {total_income}")
    return 

while True:
   transaction = get_transaction()
   transactions.append(transaction)

   balance, total_income, total_expense = calculate_totals(transactions)
   show_summary(balance, total_income, total_expense)

   again = input ("“Add another transaction? (y/n)”")
   if again.lower() != "y":
     break 
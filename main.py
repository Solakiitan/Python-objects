from budget import Budget

food = Budget()
clothing = Budget()
entertainment = Budget()

food.deposit(500)

clothing.acceptTransfer(food.makeTransfer(200))
print(clothing.balance)
print(food.balance)
entertainment.withdraw(200)


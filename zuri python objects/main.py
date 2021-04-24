from budget import Budget

food = Budget()
clothing = Budget()
entertainment = Budget()

food.deposit(500)
clothing.deposit(600)
entertainment.deposit(1000)

food.withdraw(300)
clothing.withdraw(800)
entertainment.withdraw(800)

print("Balance after withdrawing")
print(food.balance)
print(clothing.balance)
print(entertainment.balance)

print("Balance after transferring")
food.acceptTransfer(clothing.makeTransfer(300))
entertainment.acceptTransfer(food.makeTransfer(200))

print(food.balance)
print(clothing.balance)
print(entertainment.balance)
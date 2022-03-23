from bank_account import BankAccount
from savings_acc import Savings
from current_acc import Current

customer1 = Current("Liz Robson")
customer1savings = Savings("Liz Robson")
customer1.display_balance()
customer1.deposit(300)
customer1.display_balance()
customer1.withdraw(500)
customer1.overdraft()
customer1.deposit(1000)

customer1savings.deposit(500)

customer1.display_balance()
customer1savings.display_balance()

customer1.confirm_account_type()
customer1savings.confirm_account_type()

customer1savings.annual_int()

# # Setting up accounts
# customer1savings = Savings('Liz Robson')
# customer1current = Current('Liz Robson')
#
# # Setting up account numbers
# customer1savings.account_num()
# customer1current.account_num()
#
# # Withdrawing money from current account
# customer1current.withdraw()
#
# # Checking whether overdraft has been reached
# customer1current.overdraft()
#
# # Depositing money in your accounts (option to put in savings or current account
# customer1current.deposit()
#
# # Calculating interest in savings account based on current balance
# customer1savings.deposit()
# customer1savings.annual_int()
#
# # Checking balances (option to check savings or current)
# customer1savings.display_balance()
# customer1current.display_balance()
#
# # Moving money from current to savings account
# customer1current.move_money()
#
# # Confirming total balance of accounts
# customer1.total_balance()
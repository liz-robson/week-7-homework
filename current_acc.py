from bank_account import BankAccount

import random


class Current(BankAccount):

    sort_code = 123457

    def __init__(self, name):
        super().__init__(name)
        print('You have opened a Python Current Account,', self._name)
        self._account_num = int(random.randint(80000000, 89999999))
        self.account_type = "current"

    def confirm_account_type(self):
        print(f"This is your {self.account_type} account")

    def account_num(self):
        print('Your current account number is', self._account_num)

    def overdraft(self):
        if self._balance <= -200:
            print('You have reached your overdraft limit, please contact the bank to discuss your options')
        else:
            print('A reminder that your overdraft limit is £200')

    # def move_money(self, amount):
    #     self._balance -= amount
    #     print(f"You have moved £{amount} to your savings account")
    #     dest.desposit(amount)

    # def move_money(self, amount):
    #     self.main_account.current_acc.current_transfer(amount)

    # def overdraft(self):
    #     if self._current_balance <= -200:
    #         print('You have reached your overdraft limit, please contact the bank to discuss your options')
    #     else:
    #         print('A reminder that your overdraft limit is £200')
    #
    # def move_money(self):
    #     transfer = float(input("How much would you like to put in your savings account?"))
    #     self._current_balance -= transfer
    #     self._savings_balance += transfer
    #     print(f"You have moved £{transfer} from your current account to your savings account")
    #     print(f"You now have £{self._current_balance} in your current account and £{self._savings_balance} in your savings account")
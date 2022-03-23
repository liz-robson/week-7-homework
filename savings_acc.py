from bank_account import BankAccount

import random


class Savings(BankAccount):

    sort_code = 123456

    def __init__(self, name):
        super().__init__(name)
        print('You have opened a Python Savings Account,', self._name)
        self._account_num = int(random.randint(40000000, 49999999))
        self.account_type = "savings"

    def confirm_account_type(self):
        print(f"This is your {self.account_type} account")

    def account_num(self):
        print('Your savings account number is', self._account_num)

    def annual_int(self):
        interest = 0.01 * self._balance
        print('The annual interest on your savings account is', interest)
        self._balance = interest + self._balance
        print('Your new balance is', self._balance)

    # def current_transfer(self, amount):
    #     print(f"You have transferred £{amount} from your current account into your savings account")










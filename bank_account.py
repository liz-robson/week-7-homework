
class BankAccount:

    _balance = 0

    def __init__(self, name):
        self._name = name
        print('Welcome to Python Bank,', self._name)

    def display_balance(self):
        print(f"Your balance is £{self._balance}")

    def deposit(self, deposit_amount):
        print(f"You have deposited £{deposit_amount}")
        self._balance += deposit_amount
        print(f"Your balance is now £{self._balance}")

    def withdraw(self, withdraw_amount):
        print(f"You have withdrawn £{withdraw_amount}")
        self._balance -= withdraw_amount
        print(f"Your balance is now £{self._balance}")


    # def display_balance(self):
    #     display_type = input("Which balance would you like to see? Savings (S) or Current (C)?")
    #     if display_type == 'S':
    #         print(f'Your savings account balance is £{self._savings_balance}')
    #     elif display_type == 'C':
    #         print(f'Your current account balance is £{self._current_balance}')
    #     else:
    #         print('Please type Savings (S) or Current (C)')

    # def deposit(self):
    #     deposit_type = input("Which account would you like to deposit money into? Savings (S) or Current (C)")
    #     if deposit_type == 'C':
    #         deposit_amount = float(input("How much would you like to deposit?"))
    #         self._current_balance += deposit_amount
    #         print('Your current account balance is now £', self._current_balance)
    #     elif deposit_type == 'S':
    #         deposit_amount = float(input("How much would you like to deposit?"))
    #         self._savings_balance += deposit_amount
    #         print('Your savings account balance is now £', self._savings_balance)
    #     else:
    #         print('Please type (S) for Savings or (C) for Current Account')

    # def withdraw(self):
    #     withdraw_amount = float(input("How much would you like to withdraw from your account?"))
    #     self._current_balance -= withdraw_amount
    #     print('Your current account balance is now £', self._current_balance)

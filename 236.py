class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, dep):
        if dep <= 0:
            print("The amount must be greater than 0")

        else:
            self._balance += dep

    def withdraw(self, am):
        if am <= 0:
            print('the amount must be greater than 0')

        elif am > self.__balance:
            print('Insufficient funds in the account')

        else:
            self.__balance -= am

    def get_balance(self):
        return self.__balance





import datetime
import pytz


class Account:
    """ simple account class with balance"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = []
        self._transaction_list.append((Account._current_time(), balance))
        print("Account created for " + self._name)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("The amount must ne greater than 0 and no more than your account balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transaction(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (localtime was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    naqeeb = Account("Naqeeb", 0)
    naqeeb.show_balance()

    naqeeb.deposit(1000)
    # naqeeb.show_balance()
    naqeeb.withdraw(500)
    # naqeeb.show_balance()

    naqeeb.withdraw(2000)

    naqeeb.show_transaction()

    ahsan = Account("Ahsan", 800)
    ahsan.__balance = 200
    ahsan.deposit(100)
    ahsan.withdraw(200)
    ahsan.show_transaction()
    ahsan.show_balance()
    print(ahsan.__dict__)
    ahsan._Account__balance = 40   # to access private member of class 'MANGlING' rule
    ahsan.show_balance()

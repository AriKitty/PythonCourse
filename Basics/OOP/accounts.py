import datetime
import pytz


class Account:
    """ Simple account class with balance """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self._balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        print('Account created for ' + self.name)
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount < self._balance:
            self._balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("The amount must be greater than 0 and no more than your account balance")
        self.show_balance()

    def show_balance(self):
        print(f"Balance is {self._balance}")

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print(f"${amount:6} {tran_type} on {date} (local time was {date.astimezone()})")


if __name__ == "__main__":
    ari = Account("Arianna", 0)
    ari.show_balance()
    ari.deposit(1000)
    ari.withdraw(500)
    ari.withdraw(2000)
    ari.show_transactions()

    cat = Account("Cat", 800)
    cat.deposit(100)
    cat.withdraw(200)
    cat.show_transactions()

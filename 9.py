

class Bank:

    def __init__(self):
        self.money = 0

    def deposit(self, money):
        money = self._process_transaction(money)
        self.money += money

    def _process_transaction(self, money):
        return money


class ShadyBank(Bank):
    def _process_transaction(self, money):
        return money * 0.99


class AwesomeBank(Bank):
    def _process_transaction(self, money):
        return money + 1,000,000

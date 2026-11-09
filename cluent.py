class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def charge(self, amount):
        if amount > self.balance or amount < 0:
            return False

        self.balance -= amount
        return True
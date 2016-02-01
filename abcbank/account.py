from abcbank.transaction import Transaction

class Account:
    def __init__(self, accountType):
        self.accountType = accountType
        self.transactions = []
        self.balance = 0

    def deposit(self, amount):
        if not amount > 0:
            raise ValueError("Must enter an amount greater than zero")
        new_transaction = Transaction(amount,'deposit')
        self.balance += amount
        self.transactions.append(new_transaction)

    def withdraw(self, amount):
        if not amount > 0:
            raise ValueError("Must enter an amount greater than zero")
        if not self.balance >= amount:
            raise ValueError("Insufficient Funds")
        else:
            new_transaction = Transaction(amount,'withdrawl')
            self.balance -= amount
            self.transactions.append(new_transaction)

    def sumTransactions(self, checkAllTransactions=True):
        return sum([t.amount for t in self.transactions])

    def interestEarned(self):
        default_interest = self.balance * 0.001
        second_tier_interest = self.balance * 0.002
        
        if self.accountType == 'CHECKING':
            return default_interest

        elif self.accountType == 'SAVINGS':
            if self.balance <= 1000:
                 return default_interest
            else:
                return 1 + (self.balance - 1000) * 0.002

        elif self.accountType == 'MAXI_SAVINGS':
            if self.balance <= 1000:
                return second_tier_interest
            elif self.balance <= 2000:
                return 20 + (self.balance - 1000) * 0.05
            else:
                return 70 + (self.balance - 2000) * 0.1

       
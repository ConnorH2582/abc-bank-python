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
            new_transaction = Transaction(amount,'withdrawal')
            self.balance -= amount
            self.transactions.append(new_transaction)    


    def sumTransactions(self, checkAllTransactions=True):
        return sum([t.amount for t in self.transactions])

    def interestEarned(self):
        default_interest = self.balance * 0.001
        
        if self.accountType == 'CHECKING':
            return default_interest

        elif self.accountType == 'SAVINGS':
            if self.balance <= 1000:
                 return default_interest
            else:
                return 1 + (self.balance - 1000) * 0.002

        elif self.accountType == 'MAXI_SAVINGS':
            recentWithdrawal = False
            for t in self.transactions:
                if t.action == "withdrawal" and (datetime.now - t.transactionDate).days < 10:   
                    recentWithdrawal = True
            if recentWithdrawal:
                return default_interest
            else:
                return self.balance * 0.05



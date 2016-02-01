from abcbank.transaction import Transaction
import datetime
from datetime import datetime, timedelta

class Account:
    def __init__(self, accountType):
        self.accountType = accountType
        self.dateOpened = datetime.now()
        self.transactions = []
        self.balance = 0
        self.account_age_in_days = (datetime.now() - self.dateOpened).days


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

    def dailyInterestRate(self):
        default_interest = self.balance * 0.001 / 356
        if self.accountType == 'CHECKING':
            interest = (default_interest)

        elif self.accountType == 'SAVINGS':
            if self.balance <= 1000:
                interest = default_interest
            else:
                interest = (1 + (self.balance - 1000) * 0.002) / 356 

        elif self.accountType == 'MAXI_SAVINGS':
            for t in self.transactions:
                if t.action == "withdrawal" and (datetime.now() - t.transactionDate).days < 10:   
                    interest = default_interest
                else:
                    interest = self.balance * 0.05 / 356
        return interest

    def interestEarnedDaily(self):
        interest = 0
        if self.account_age_in_days > 0:
            for day in range(self.account_age_in_days-1):
                interest += self.dailyInterestRate()
        return interest

    def accrueInterest(self):
        for day in range(self.account_age_in_days-1):
            self.balance += self.accruedDailyInterest() * self.interestEarnedDaily
        return self.balance






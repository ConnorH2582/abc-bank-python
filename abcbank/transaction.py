from datetime import datetime


class Transaction:
    def __init__(self,amount,action):
        self.amount = amount
        self.transactionDate = datetime.now()
        self.action = action


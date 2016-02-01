from .account import Account


class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def openAccount(self, account_type):
        is_valid = ['CHECKING','SAVINGS','MAXI_SAVINGS']
        if account_type in is_valid:
            new_account = Account(account_type)
            self.accounts.append(new_account)
            return new_account
        else:
            raise ValueError("Invalid Account Type")
            
    def numAccs(self):
        return len(self.accounts)

    def totalInterestEarned(self):
        return sum([a.interestEarned() for a in self.accounts])

    def totalAssets(self):
        return "Total Assets: " + _toDollars(sum([a.balance for a in self.accounts]))

    # This method gets a statement
    def getStatement(self):
        # JIRA-123 Change by Joe Bloggs 29/7/1988 start
        statement = None  # reset statement to null here
        # JIRA-123 Change by Joe Bloggs 29/7/1988 end
        totalAcrossAllAccounts = sum([a.sumTransactions() for a in self.accounts])
        statement = "Statement for %s" % self.name
        for account in self.accounts:
            statement = statement + self.statementForAccount(account)
        statement += "\n\nTotal In All Accounts " + _toDollars(totalAcrossAllAccounts)
        return statement

    def statementForAccount(self, account):
        accountType = "\n\n\n"
        if account.accountType == 'CHECKING':
            accountType = "\n\nChecking Account\n"
        if account.accountType == 'SAVINGS':
            accountType = "\n\nSavings Account\n"
        if account.accountType == 'MAXI_SAVINGS':
            accountType = "\n\nMaxi Savings Account\n"
        transactionSummary = [t.action + " " + _toDollars(t.amount) for t in account.transactions]
        transactionSummary = "  " + "\n  ".join(transactionSummary) + "\n"
        totalSummary = "Total " + _toDollars(sum([t.amount for t in account.transactions]))
        return accountType + transactionSummary + totalSummary

    def makeTransfer(self,amount,account_to,account_from):
        deposit_to = account_to.deposit(amount)
        withdraw_from = account_from.withdraw(amount)
        return self.getStatement()

def _toDollars(number):
    return "${:1.2f}".format(number)


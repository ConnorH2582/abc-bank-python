from nose.tools import assert_equals, nottest
from abcbank.bank import Bank
from abcbank.account import Account
from abcbank.customer import Customer
from abcbank.transaction import Transaction


def test_statement():
    bank = Bank()
    henry = bank.addCustomer("Henry")
    henry_checking=henry.openAccount('CHECKING')
    henry_savings = henry.openAccount('SAVINGS')
    henry_checkings.deposit(100.0)
    henry_savings.deposit(4000.0)
    henry_savings.withdraw(200.0)
    assert_equals(henry.getStatement(),
                  "Statement for Henry" +
                  "\n\nChecking Account\n  deposit $100.00\nTotal $100.00" +
                  "\n\nSavings Account\n  deposit $4000.00\n  withdrawal $200.00\nTotal $3800.00" +
                  "\n\nTotal In All Accounts $3900.00")


def test_oneAccount():
    bank = Bank()
    oscar = bank.addCustomer("Oscar")
    oscar_savings = oscar.openAccount('SAVINGS')
    assert_equals(oscar.numAccs(), 1)

def test_twoAccounts():
    bank = Bank()
    oscar = bank.addCustomer("Oscar")
    oscar_savings = oscar.openAccount('SAVINGS')
    oscar_checking = oscar.openAccount('CHECKING')
    assert_equals(oscar.numAccs(), 2)

@nottest
def test_threeAccounts():
    bank = Bank()
    oscar = bank.addCustomer("Oscar")
    oscar_savings = oscar.openAccount('SAVINGS')
    oscar_checking = oscar.openAccount('CHECKING')
    oscar_checking = oscar.openAccount('MAXI_SAVINGS')
    assert_equals(oscar.numAccs(), 3)

if __name__ == '__main__':
    test_oneAccount()
    test_twoAccounts()
    test_threeAccounts()


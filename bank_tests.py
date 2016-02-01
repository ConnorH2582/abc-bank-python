from nose.tools import assert_equals
from abcbank.account import Account
from abcbank.bank import Bank
from abcbank.customer import Customer
from abcbank.transaction import Transaction


def test_customer_summary():
    bank = Bank()
    john = bank.addCustomer('John')
    john_new_checking = john.openAccount('CHECKING')
    assert_equals(bank.customerSummary(),"Customer Summary\n - John (1 account)")

def test_checking_account():
    bank = Bank()
    bill = bank.addCustomer("Bill")
    bill_new_checking = bill.openAccount('CHECKING')
    bill_new_checking.deposit(100.00)
    assert_equals(bank.totalInterestPaid(), .1)

def test_savings_account():
    bank = Bank()
    bill = bank.addCustomer("Bill")
    bill_new_savings = bill.openAccount('SAVINGS')
    bill_new_savings.deposit(1500.0)
    assert_equals(bank.totalInterestPaid(), 2.0)

def test_maxi_savings_account():
    bank = Bank()
    bill = bank.addCustomer("Bill")
    bill_new_maxi = bill.openAccount('MAXI_SAVINGS')
    bill_new_maxi.deposit(3000.0)
    assert_equals(bank.totalInterestPaid(), 170.0)

if __name__ == '__main__':
    test_customer_summary()
    test_checking_account()
    test_savings_account()
    test_maxi_savings_account()
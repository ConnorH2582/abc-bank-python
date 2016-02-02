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
    bill_new_checking.account_age_in_days = 20
    assert_equals(round(bank.totalInterestPaid(),3), .005)

def test_savings_account():
    bank = Bank()
    bill = bank.addCustomer("Bill")
    bill_new_maxi = bill.openAccount('MAXI_SAVINGS')
    bill_new_maxi.deposit(1500.0)
    bill_new_maxi.account_age_in_days = 10
    assert_equals(round(bill_new_maxi.interestEarnedDaily(),2),1.9)

def test_maxi_savings_account():
    bank = Bank()
    bill = bank.addCustomer("Bill")
    bill_new_maxi = bill.openAccount('MAXI_SAVINGS')
    bill_new_maxi.deposit(3000.0)

def test_transfer():
    bank = Bank()
    bill = bank.addCustomer("Bill")
    bill_savings = bill.openAccount('SAVINGS')
    bill_checking = bill.openAccount('CHECKING')
    bill_savings.deposit(200.0)
    bill_checking.deposit(100.0)
    bill.makeTransfer(50.0,bill_savings,bill_checking)
    assert_equals(bill_checking.balance,50.0)
    assert_equals(bill_savings.balance,250.0)

if __name__ == '__main__':
    test_customer_summary()
    test_checking_account()
    test_savings_account()
    test_maxi_savings_account()
    test_transfer()
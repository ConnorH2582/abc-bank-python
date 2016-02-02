from nose.tools import assert_is_instance,assert_equal
from abcbank.account import Account
from abcbank.customer import Customer
from abcbank.transaction import Transaction
from abcbank.bank import Bank


def test_withdrawal():
    t = Transaction(5,'withdrawal')
    assert_is_instance(t, Transaction)
    assert_equal(t.action, 'withdrawal')
    assert_equal(t.amount, 5)

def test_deposit():
    t = Transaction(5,'deposit')
    assert_is_instance(t, Transaction)
    assert_equal(t.action, 'deposit')

if __name__ == '__main__':
	test_withdrawal()
	test_deposit()

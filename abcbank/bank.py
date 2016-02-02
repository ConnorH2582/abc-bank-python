from abcbank.customer import Customer

class Bank:
    def __init__(self):
        self.customers = []

    def addCustomer(self, customer_name):
        new_customer = Customer(customer_name)
        self.customers.append(new_customer)
        return new_customer
    
    def customerSummary(self):
        summary = "Customer Summary"
        for customer in self.customers:
            summary += "\n - " + customer.name + " (" + self._format(customer.numAccs(), "account") + ")"
        return summary

    def _format(self, number, word):
        return str(number) + " " + (word if (number == 1) else word + "s")

    def totalInterestPaid(self):
        total = 0
        for c in self.customers:
            total += c.totalInterestEarned()
        return total

    def getFirstCustomer(self):
        if self.customers:
            return self.customers[0].name
        else:
            return "Error"
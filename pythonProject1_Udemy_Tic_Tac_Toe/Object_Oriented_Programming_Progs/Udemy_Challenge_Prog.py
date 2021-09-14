class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return 'Account Owner: ' + self.owner + "\n" + 'Account Balance: '+ str(self.balance)
        # return f"Owner: {self.owner} \nBalance: {self.balance}"

    def deposit(self, amt):
        self.balance += amt
        print('Deposit Accepted!')

    def withdraw(self, amt):
        if self.balance >= amt:
            self.balance -= amt
            print('Withdrawal Accepted!')
        else:
            print('Funds Unavailable!')


acct1 = Account('Jose', 100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
# deposit amount 50
acct1.deposit(50)
print(acct1)

# withdraw amount 110
acct1.withdraw(110)
print(acct1)

# withdraw amount more than balance
acct1.withdraw(60)

# series of deposits
for i in [30, 45, 100]:
    acct1.deposit(i)
print(acct1)


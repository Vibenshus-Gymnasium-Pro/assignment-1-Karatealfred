class BankAccount:
    """Bank Account protected by a pin number."""

    def __init__(self, pin):
        """Initial account balance is 0 and pin is 'pin'."""
        self.pin = pin
        self.balance = 100

    def deposit(self, pin, amount):
        """Increment account balance by amount and return new balance."""
        if self.pin == pin:
            self.balance += amount
            print('You deposited', amount)
            print('Your balance is now', self.balance)
        else:
            print('Pin was wrong')


    def withdraw(self, pin, amount):
        """Decrement account balance by amount and return amount withdrawn."""
        if self.pin == pin:
            self.balance -= amount
            print('You withdrew', amount)
            print('Your balance is now', self.balance)
        else:
            print('Pin was wrong')

    def get_balance(self, pin):
        """Return account balance."""
        if self.pin == pin:
            print('Your balance is', self.balance)
        else:
            print('Pin was wrong')

    def change_pin(self, oldpin, newpin):
        """Change pin from oldpin to newpin."""
        if oldpin == self.pin:
            self.pin = newpin
            print('Pin was changed to', self.pin)
        else:
            print('Pin was wrong')

class SavingsAccount(BankAccount):
    def __init__(self, pin):
        super().__init__(pin)
        self.interest = 0.02

    def get_interest(self, pin):
        if pin == self.pin:
            self.balance = self.balance * (1+self.interest)
            print('Your balance is now', self.balance)
        else:
            print('Wrong pin')

class FeeSavingsAccount(SavingsAccount):
    def __init__(self, pin):
        super().__init__(pin)
        self.fee = 3

    def withdraw(self, pin, amount):
        """Decrement account balance by amount and return amount withdrawn."""
        if self.pin == pin:
            if self.balance >= amount + self.fee:
                self.balance -= amount + self.fee
                print('You withdrew', amount)
                print('Your balance is now', self.balance)
            else:
                print('Your balance is to low')
        else:
            print('Pin was wrong')

x = FeeSavingsAccount(1234)
x.withdraw(1234, 40)
x.withdraw(1233, 10)
x.withdraw(1234, 55)
x.get_interest(1234)
x.change_pin(1234, 4321)
x.deposit(4321, 30)
x.get_balance(4321)
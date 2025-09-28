# module7.py
# Demonstrates classes, instances, and hidden attributes in Python

class Account:
    # Class attribute (shared by all accounts)
    bank_name = "Bizecurity Credit Union"

    def __init__(self, owner, opening_balance):
        self.owner = owner                      # public attribute
        self.__balance = float(opening_balance) # hidden (name-mangled)

    # Property to safely access balance
    @property
    def balance(self):
        return self.__balance

    # Setter with validation
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self.__balance = float(amount)

    # Deposit method
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.__balance += amount
        return self.__balance

    # Withdraw method
    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount
        return self.__balance

    # String representation
    def __repr__(self):
        return f"Account(owner={self.owner!r}, balance={self.__balance:.2f})"


# --- Example usage ---
if __name__ == "__main__":
    # Create instances (objects) from the class
    acct1 = Account("Stacey", 100)
    acct2 = Account("Jordan", 250)

    print("Bank name:", Account.bank_name)
    print(acct1)     # Account(owner='Stacey', balance=100.00)
    print(acct2)     # Account(owner='Jordan', balance=250.00)

    # Work with balance using methods/properties
    acct1.deposit(50)
    print("Stacey's balance after deposit:", acct1.balance)

    acct2.withdraw(100)
    print("Jordan's balance after withdrawal:", acct2.balance)

    # Trying to access hidden attribute directly will fail:
    # print(acct1.__balance)   # AttributeError
    # But it's still stored as a mangled name:
    print("Access via mangled name (not recommended):", acct1._Account__balance)

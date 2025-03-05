# ## Bank
# 1. acc_no
# 2. name
# 3. balance

# ```py
# print(diyali.deposit(5_000))  # Successfully deposited. Your balance is: R65,000.00
# print(diyali.display_balance())  # Your balance is: R65,000.00
# print(diyali.withdraw(1_000)) # Success. Your balance is: R64,000.00
# ```


class Bank:
    interest_rate = 0.02
    count = 0

    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        Bank.count += 1

    def display_balance(self):
        return f"Your balance is R{self.balance:,.2f}"

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            return f"Success. {self.display_balance()}"
        elif amount > self.balance:
            return "Invalid amount"
        else:
            return f"Insufficient funds. {self.display_balance()}"

    def deposit(self, amount):
        if amount < 0:
            return "Invalid amount"
        else:
            self.balance += amount
            return f"Sucessfully deposited. {self.display_balance()}"

    def apply_interest(self):
        self.balance += self.interest_rate * self.balance
        return f"Success. {self.display_balance()}"

    @classmethod
    def update_interest_rate(cls, interest_rate):
        if 0 < interest_rate < 100:
            cls.interest_rate = interest_rate / 100
            return f"Interest rate updated to {interest_rate}%"
        else:
            return f"Invalid interest rate"

    @classmethod
    def get_total_no_accounts(cls):
        return f"In total we have {cls.count} accounts"


class SavingsAccount(Bank):
    interest_rate = 0.05


class CheckingAccount(Bank):
    transact_fee = 1

    def withdraw(self, amount):
        return super().withdraw(amount + self.transact_fee)


chleo = Bank(123456789, "Chleo Smith", 100_000)
diyali = Bank(987654321, "Diyali Devraj", 60_000)
jevan = Bank(654789123, "Jevan Peters", 800_000)

print(chleo.withdraw(2000))
print(chleo.display_balance())

chelo = SavingsAccount(123, "Chleo Smith", 100_000)
anita = CheckingAccount(123, "Anita", 50_000)
print(diyali.apply_interest())
print(chelo.apply_interest())
print(anita.withdraw(1000))


# print(diyali.deposit(5_000))  # Successfully deposited. Your balance is: R65,000.00
# print(diyali.display_balance())  # Your balance is: R65,000.00
# print(diyali.withdraw(1_000))  # Success. Your balance is: R64,000.00


# print("\n")

# print(diyali.apply_interest())
# print(diyali.update_interest_rate(105))
# print(Bank.get_total_no_accounts())


# Task 1.8 & Task 1.9
# 1.  SavingsAccount - 5%
# 2.  CheckingAccount - R1 - transaction fee, Interest rate does not change

# ```py
# chelo = SavingsAccount(123, "Chleo Smith", 100_000)
# ```

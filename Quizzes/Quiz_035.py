import random

class Account:
    def __init__(self):
        self.balance = 0
        self.holder_name = ""
        self.holder_email = ""
        num1 = random.randint(100, 999)
        num2 = random.randint(10000, 99999)
        num3 = random.randint(0, 9)
        self.number = [f"{num1}-{num2}-{num3}"]

    def get_account_no(self):
        return self.number[0]

    def set_holder_name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        self.holder_name = name
        temp = f"Holder's name set to {self.holder_name}"
        return temp

    def set_holder_email(self, email):
        self.holder_email = email
        temp = f"Holder's email set to {self.holder_email}"
        return temp

    def get_balance(self):
        return self.balance

    def deposit(self, amount:int):
        self.balance += amount
        temp = f"New balance: {self.balance} USD"
        return temp
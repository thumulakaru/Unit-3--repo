class CompoundInterest:
    def __init__(self, principal:int, rate:float, year:int):
        self.principal = principal
        self.rate = rate
        self.year = year


class AccountingProgram:
    def __init__(self):
        self.compound = CompoundInterest(0, 0, 0)

    def set_principal(self, principal):
        if principal <= 0:
            raise ValueError("Principal should be greater than zero")
        self.compound.principal = principal
        return f"Principal set to {self.compound.principal}"

    def set_rate(self, rate):
        if rate <= 0:
            raise ValueError("Interest rate should be greater than zero")
        self.compound.rate = rate
        return f"Rate set to {self.compound.rate}"

    def set_years(self, year):
        if year <= 0:
            raise ValueError("Years should be greater than zero")
        self.compound.year = year
        return f"Year set to {self.compound.year}"

    def calculate_interest(self):
        temp1 = self.compound.principal * (self.compound.rate + 1) ** self.compound.year
        temp_f = "{:.2f}".format(temp1)
        return float(temp_f)

class Investment:
    def __init__(self, principal, interest_rate, years):
        self.principal = principal
        self.interest_rate = interest_rate
        self.years = years
    
    def calculate_future_value(self):
        future_value = self.principal * (1 + self.interest_rate) ** self.years
        return future_value



principal_amount = float(input("Enter the principal amount: "))

interest_rate = float(input("Enter the interest rate : "))

num_of_years = int(input("Enter the number of years: "))

investment = Investment(principal_amount, interest_rate, num_of_years)

future_value = investment.calculate_future_value()

print(f"The future value of the investment is: {future_value}")

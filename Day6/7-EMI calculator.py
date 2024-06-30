
principal = float(input("Enter the loan amount: "))
period = float(input("Enter the loan period in months: "))
annual_rate = float(input("Enter the annual interest rate (in %): "))

monthly_rate = annual_rate / (12 * 100)
number_of_payments = period

emi = principal * monthly_rate * (1 + monthly_rate) ** number_of_payments / ((1 + monthly_rate) ** number_of_payments - 1)

print(f"Monthly EMI: {emi}")

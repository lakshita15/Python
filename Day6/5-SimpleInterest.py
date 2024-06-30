
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time in years: "))


simple_interest = (principal * rate * time) / 100
compound_amount = principal * (1 + (rate / 100)) ** time
compound_interest = compound_amount - principal

print(f"Simple Interest: {simple_interest}")
print(f"Compound Interest: {compound_interest}")
print(f"Total Amount (with Compound Interest): {compound_amount}")


cost = float(input("Enter the cost of the item: "))

discount_percentage = float(input("Enter the discount percentage: "))

discount_amount = (discount_percentage / 100) * cost


sale_price = cost - discount_amount

print(f"Discount amount: {discount_amount}")
print(f"Sale price: {sale_price}")

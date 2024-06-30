
cost_price = float(input("Enter the cost price of the item: "))
selling_price = float(input("Enter the selling price of the item: "))

# Calculate profit or loss
profit_loss = selling_price - cost_price

if profit_loss > 0:
    print(f"Profit: {profit_loss}")
elif profit_loss < 0:
    print(f"Loss: {-profit_loss}")
else:
    print("No profit, no loss.")
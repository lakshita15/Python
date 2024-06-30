price = float(input("Enter the price of the item: "))
gst_rate = float(input("Enter the GST rate (in %): "))


gst_amount = (gst_rate / 100) * price
total_price = price + gst_amount

print(f"GST Amount: {gst_amount}")
print(f"Total Price (including GST): {total_price}")

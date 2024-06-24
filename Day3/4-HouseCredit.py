HousePrice = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1*HousePrice
else:
     down_payment = 0.2*HousePrice

print(f"${down_payment}")
#pound to kg
#l for pound or k for kg

weight = int(input("enter your weight"))
unit = input("enter unit, k for kg and l for lb")

if unit.upper() =="L":
    weight = weight * 0.45
    print(weight)
elif unit.upper() == "K":
    weight = weight // 0.45
    print(weight)
else:
    print("enter valid input")
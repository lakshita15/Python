name = input("enter name")
name_len = len(name)

if name_len < 3:
    print("name must be at least three characters")
elif name_len >50:
    print("name must be at max 50 characters")
else:
    print("good name")
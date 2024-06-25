
Secret_number = 4
Guess_count=0
while Guess_count < 3:
    guess= int(input("enter your guess number between 1-9. You have 3 chances"))
    Guess_count +=1
    if guess == Secret_number:
        print("you won")
        break
else:
    print("sorry, you lost")
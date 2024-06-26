command = ""

while command!='QUIT':
    command = input("> ").upper()
    if command=='START':
        print("Car Started")
    elif command=='STOP':
        print("car stopped")
    elif command=='HELP':
        print("Enter start - to start car")
        print("Enter stop - to start car")
        print("Enter quit - to start car")  
    elif command=='QUIT':
        break
    else :
        print("I don't understand that")
       
        

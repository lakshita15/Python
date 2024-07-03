#Write a function to find the longest word in a list of words.

list = input("Enter list of words seperated by , ").split(",")
length = len(list[0])
# print(length)
for i in list:
    # print(i)
    if len(i)>length:
        length = len(i)
        print(i)
    

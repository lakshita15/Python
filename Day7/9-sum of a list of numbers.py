#Write a function to calculate the sum of a list of numbers.

def sum (list_of_no):
    sum = 0
    for i in list_of_no:
        sum+=i

    return sum


list_in = list(map(int,input("Enter a list seperated by space: ").split(" ")))
print(list_in)
ans = sum(list_in)
print(ans)
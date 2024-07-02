#Problem: Write a function to find the factorial of a number.
def factorial(num):
    print(num)
    ans = 1
    while num > 0 :
        print(f"in while",{num})
        ans *= num
        num-=1

    return ans


number = int(input("Enter number you want to get factorial for:- "))
ans = factorial(number)
print(ans)

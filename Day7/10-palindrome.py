def palindrome(s):
    p1 = 0
    p2 = len(s) - 1
    while p1 < p2:
        if s[p1] != s[p2]:
            return False
        p1 += 1
        p2 -= 1
    return True

string = input("Enter a string: ")
string_palin = palindrome(string)
print(f"Is the string a palindrome? {string_palin}")
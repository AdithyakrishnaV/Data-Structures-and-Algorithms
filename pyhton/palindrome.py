def palindrome(s):
    return s == s[::-1]

s="malayalam"
result=palindrome(s)
# print(result)

if result:
    print("Yes it is palindrome")
else:
    print("It is not palindrome")

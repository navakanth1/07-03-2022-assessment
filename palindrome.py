def palindrome(str):
    if str == str[::-1]:
        return true
    else:
        return false
string = input("appa isi ")
result = palindrome(string)
if result:
    print("str is palindrome")
else:
    print("str is not palindrome")



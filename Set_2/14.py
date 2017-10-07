def palindrome(inp):
    a = inp[::-1]

    if inp == a:
        print("Yes! Palindrome..")
    else:
        print("No! Not Palindrome..")
palindrome("ana")
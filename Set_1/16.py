inp = input("Enter a fruit name:")
vowel = "aeiouAEIOU"


if inp[0] in vowel:
    print("This is an " + inp)
else:
    print("This is a " + inp)
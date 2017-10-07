ch = int(input('''
1. Celsius
2. Fahrenheit
Enter the temperature in:
'''))

if ch == 1:
    inp1 = int(input("Enter temperature in Censius: "))
    out1 = float(((9*inp1)+160)/5)
    print(inp1, "Celsius equal", out1, "Fahrenheit")

else:
    inp2 = int(input("Enter temperature in Fahrenheit: "))
    out2 = float((5*(inp2-32))/9)
    print(inp2, "Fahrenheit equal", out2, "Celsius")
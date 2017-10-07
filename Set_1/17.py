def _sum(x, y):
    return x + y

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = _sum(a, b)

if c > 21 and a or b == 11:
    c = c - 10
    
print(c)
        
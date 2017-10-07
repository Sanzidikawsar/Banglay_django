inp = int(input("Enter length of series: "))
fin = []
even = 0
odd = 0

for i in range(1, inp):
    fin.append(i)
    if i%2 != 0:
        odd += 1
    else:
        even += 1
print("Number of odd numbers is: ", odd)
print("Number of even numbers is: ", even)
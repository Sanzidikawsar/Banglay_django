inp = int(input())

if (inp%2 != 0) or (inp%2 == 0) and ((inp > 20) or (inp in range(11, 21))):
    print("Weird!")
    
elif inp%2 == 0 and inp in range(2,11):
    print("Not Weird!")
    
elif inp%2 == 0 and inp in range(11, 21):
    print("Weird!")
    
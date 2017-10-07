count = 0 

for i in range(2017,2117):
    if i%4 == 0:
        if i%100 == 0:
            if i%400 ==0:
                print(count+1, i)
                count += 1

        print(count+1, i)
        count += 1
    if count == 20:
        break
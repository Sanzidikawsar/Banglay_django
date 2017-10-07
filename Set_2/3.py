inp = ['abc', 'xyz', 'aba', '1221']
count = 0

for i in inp:
    if len(i) > 1 and i[0] == i[-1]:
        count = count + 1

print(count)
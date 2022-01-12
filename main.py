total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total += i
print(total)

                    # OR
total2 = 0
for num in range(0, 101, 2):
    total2 += num
print( total2)
# Print numbers from 1 to 30, but skip all multiples of 4 using continue.

for i in range(1,31):
    if i%4==0:
        continue
    print(i)